#!/usr/bin/env python3
"""Read-only Docker/configuration export into a private directory outside Git."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request
from urllib.parse import urlsplit

MAX_CONFIG = 8 * 1024 * 1024

def validate_output(output: Path, collection: Path) -> Path:
    output, collection = Path(output), Path(collection)
    if output.absolute().is_relative_to(collection.absolute()) or output.resolve().is_relative_to(collection.resolve()):
        raise ValueError('Private snapshots must be outside the collection')
    for parent in [output.resolve(), *output.resolve().parents]:
        if (parent / '.git').exists():
            raise ValueError('Private snapshots must not be written into any Git checkout')
    if output.exists():
        raise FileExistsError('Choose a new output directory; existing backups are never overwritten')
    return output.resolve()

def write_private(path: Path, data: bytes) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, 'wb') as file:
        file.write(data)

def docker(*args: str) -> bytes:
    result = subprocess.run(['docker', *args], capture_output=True)
    if result.returncode:
        raise RuntimeError('Docker read command failed; no configuration was changed')
    return result.stdout

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--collection', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--extra-compose', action='append', default=[], type=Path)
    parser.add_argument('--config-file', action='append', default=[], help='Explicit CONTAINER:/absolute/config-file to capture')
    parser.add_argument('--coolify-url', default=os.environ.get('COOLIFY_URL'), help='Optional HTTPS API or local loopback HTTP URL; token comes from COOLIFY_TOKEN')
    args = parser.parse_args()
    os.umask(0o077)
    root = validate_output(args.output, args.collection)
    root.mkdir(mode=0o700, parents=True)
    ids = docker('ps', '-aq').decode().split()
    containers = json.loads(docker('inspect', *ids)) if ids else []
    write_private(root/'docker-inspect.json', json.dumps(containers, indent=2).encode())
    image_ids = sorted({item['Image'] for item in containers})
    if image_ids:
        write_private(root/'docker-images.json', docker('image', 'inspect', *image_ids))
    paths = set(args.extra_compose)
    for item in containers:
        labels = item['Config'].get('Labels') or {}
        paths.update(Path(path.strip()) for path in labels.get('com.docker.compose.project.config_files', '').split(',') if path.strip())
    for path in list(paths):
        paths.add(path.parent/'.env')
    paths.update(args.collection.glob('*/.env'))
    paths.update(args.collection.glob('*/docker-compose.override.local.yaml'))
    captured, missing = [], []
    for path in sorted(paths):
        try:
            if not path.is_file() or path.stat().st_size > MAX_CONFIG:
                missing.append(str(path)); continue
            data = path.read_bytes()
        except (PermissionError, OSError):
            missing.append(str(path)); continue
        name = 'files/'+hashlib.sha256(str(path).encode()).hexdigest()[:16]+'-'+path.name
        write_private(root/name, data)
        captured.append({'original':str(path), 'snapshot':name, 'sha256':hashlib.sha256(data).hexdigest()})
    for value in args.config_file:
        container, separator, source = value.partition(':')
        if not separator or not source.startswith('/'):
            raise ValueError('--config-file needs CONTAINER:/absolute/path')
        data = docker('exec', '-u', '0', container, 'cat', source)
        if len(data) > MAX_CONFIG:
            raise ValueError('Requested configuration file exceeds the size bound')
        name = 'container-configs/'+hashlib.sha256(value.encode()).hexdigest()[:16]+'-'+Path(source).name
        write_private(root/name, data)
        captured.append({'container_file':value, 'snapshot':name, 'sha256':hashlib.sha256(data).hexdigest()})
    api_status = 'not requested'
    if args.coolify_url:
        endpoint = urlsplit(args.coolify_url)
        if endpoint.username or endpoint.password or endpoint.query or endpoint.fragment or not (endpoint.scheme=='https' or endpoint.scheme=='http' and endpoint.hostname in {'127.0.0.1','localhost','::1'}):
            raise ValueError('Coolify API needs HTTPS or loopback HTTP, without URL credentials')
        token = os.environ.get('COOLIFY_TOKEN')
        if not token:
            raise ValueError('Set COOLIFY_TOKEN privately to include API metadata')
        class NoRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, *unused_args, **unused_kwargs):
                return None
        opener = urllib.request.build_opener(NoRedirect)
        for resource in ['servers','applications','services']:
            request = urllib.request.Request(args.coolify_url.rstrip('/')+'/api/v1/'+resource, headers={'Authorization':'Bearer '+token,'Accept':'application/json'})
            with opener.open(request, timeout=20) as response:
                write_private(root/('coolify-'+resource+'.json'), response.read())
        api_status = 'captured'
    revision = subprocess.run(['git','-C',str(args.collection),'rev-parse','HEAD'],capture_output=True,text=True)
    manifest = {'collection_revision':revision.stdout.strip() if revision.returncode==0 else None,'containers':len(containers),'files':captured,'unavailable_source_paths':missing,'coolify_api':api_status,'configuration_only':True,'restore_tested':False}
    write_private(root/'manifest.json', json.dumps(manifest,indent=2).encode())
    write_private(root/'README.txt', b'PRIVATE: contains credentials and original paths. Keep out of Git; encrypt before off-host storage. Definitions and selected configuration files only, not application data, database dumps, remote control-plane settings or an image archive. Original source files may require privileged read access; see manifest.json for unavailable paths.\n')
    print(json.dumps({'output':str(root),'containers':len(containers),'captured_files':len(captured),'unavailable_source_paths':len(missing)}))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
