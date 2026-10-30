# Configuration backup and recovery

This collection is the public part of my service-configuration backup. The private part holds real paths, credentials, mounted configuration files and runtime/source metadata. Keep that part outside Git and in your encrypted off-host backup.

## Capture configuration

The read-only helper records Docker inspect metadata, image metadata, available source Compose/environment files and local `.env` files. Its output includes secrets, so it refuses destinations inside this or another Git checkout and creates owner-only files.

```sh
python3 tools/snapshot_configs.py --output /secure/backups/service-configs-YYYYMMDD
```

Add configuration files that live inside a service, or source files not recorded in Compose labels:

```sh
python3 tools/snapshot_configs.py \
  --output /secure/backups/service-configs-YYYYMMDD \
  --extra-compose /path/to/a/private/docker-compose.yaml \
  --config-file samba:/data/config.yml
```

Optional Coolify metadata uses `COOLIFY_TOKEN` from the environment; never put that token in this repository or a command argument. Set `--coolify-url` to the appropriate HTTPS endpoint, or a local loopback HTTP endpoint. Requests do not follow redirects with credentials.

Inspect `manifest.json` after each export: unavailable original paths are reported. Some manual containers have no source Compose label, and some configuration lives inside mounted files or application state. Supply the explicit configuration-file arguments you need. The helper does not read whole volume contents, dump databases or save container images.

## Recover on the intended machine

1. Check out the collection revision recorded with the private snapshot.
2. Restore the private `.env`, configuration files and any required local overrides. Keep host paths or adjust them deliberately in `.env`. For Samba, restore `/data/config.yml`; for the proxy, restore its static/dynamic configuration and private certificate settings.
3. Restore the existing volumes/state through your normal backup process. Select the original named volumes with `VOLUME_*_NAME` or a private override that marks them external. Keep the encryption/API keys paired with that state.
4. Restore shared networks, VPN/network-namespace dependencies and proxy ownership. Coolify-managed services should be recreated through the recovered control plane or imported deliberately; do not start duplicate services against the same data.
5. Run `docker compose --env-file .env config --quiet` and inspect the effective mounts, volume names, ports and dependencies. This validates the definition, not the application data.
6. Deploy the selected stack only when ready, then check its health, logs and actual client behaviour. Do not remove named volumes while recovering.

Image tags such as `latest` are kept where that is the running configuration. `images.lock.json` records the observed registry digest/image ID for current-use definitions; pin the appropriate recorded registry digest when recovering that version. The private snapshot also retains image metadata. A locally built image also needs its source/build or a private image backup. A Compose file alone cannot reconstruct modifications stored in a container's writable layer or a persistent code volume.

## What stays private

Real `.env` files and local overrides are ignored. Configuration directories, certificates, data, caches, media and backups are ignored too. Use `.env.example` as the public checklist; use the protected snapshot as the source of actual machine values. Do not copy a resolved configuration containing secrets into a commit.
