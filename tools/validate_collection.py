#!/usr/bin/env python3
"""Validate public examples without starting, pulling or changing containers."""
from pathlib import Path
import json
import os
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    errors = []
    env = {key: os.environ[key] for key in ['PATH','HOME','DOCKER_CONFIG'] if key in os.environ}
    files = subprocess.run(['git','ls-files','--cached','--others','--exclude-standard'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.splitlines()
    for name in sorted(set(files)):
        path = ROOT/name
        if not path.is_file():
            continue
        if path.name == '.env' or path.name.startswith('.env.') and not path.name.endswith('.example'):
            errors.append(f'{name}: private environment file must not be tracked')
        text = path.read_text(errors='replace')
        if re.search(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----',text):
            errors.append(f'{name}: private key material')
        if re.search(r'\b(?:192\.168\.\d+\.\d+|10\.\d+\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b',text):
            errors.append(f'{name}: replace private LAN addresses with parameters')
    checked = []
    for compose in sorted([*ROOT.glob('*/docker-compose.yaml'), *ROOT.glob('examples/*/docker-compose.yaml')]):
        example = compose.parent/'.env.example'
        if not example.is_file():
            errors.append(f'{compose.parent.name}: missing .env.example');continue
        combinations = [[compose]]
        gpu = compose.parent/'docker-compose.gpu.yaml'
        if gpu.exists():
            combinations.append([compose,gpu])
        for group in combinations:
            command = ['docker','compose','--env-file',str(example)]
            for file in group:
                command += ['-f',str(file)]
            result = subprocess.run(command+['config','--format','json'],env=env,capture_output=True,text=True)
            label = compose.parent.name+(' + GPU' if len(group)>1 else '')
            if result.returncode:
                errors.append(label+': Compose configuration failed: '+result.stderr.strip());continue
            data = json.loads(result.stdout)
            for name,service in data.get('services',{}).items():
                if service.get('image','').startswith(('postgres:','supabase/postgres:')) and service.get('ports'):
                    errors.append(label+'/'+name+': PostgreSQL ports must not be host-published')
                for value in service.get('volumes',[]):
                    if value.get('type')=='bind' and value.get('source','').startswith('/home/') and not Path(value['source']).resolve().is_relative_to(ROOT):
                        errors.append(label+'/'+name+': personal bind path')
            checked.append(label)
    for error in errors:
        print('FAIL: '+error,file=sys.stderr)
    print(json.dumps({'configurations_checked':len(checked),'errors':len(errors),'containers_started':0,'images_pulled':0}))
    return 1 if errors else 0

if __name__=='__main__':
    raise SystemExit(main())
