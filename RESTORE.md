# Configuration backup and recovery

The repository holds Compose files and public configuration examples. Keep actual `.env` files, private configuration and matching application/data backups separately.

## Capture configuration

```sh
python3 tools/snapshot_configs.py --output /secure/backups/service-configs
```

The helper saves Docker/image metadata and available source Compose/environment files outside Git, with owner-only permissions. Its output can contain credentials. It does not dump databases or copy entire volumes.

Additional files can be selected explicitly:

```sh
python3 tools/snapshot_configs.py \
  --output /secure/backups/service-configs \
  --extra-compose /path/to/compose.yaml \
  --config-file samba:/data/config.yml
```

## Restore

Restore the configuration, original volume identities and matching data/keys before starting the selected stack. Check paths, network dependencies and proxy ownership; then validate with `docker compose --env-file .env config --quiet`.

Keep the private snapshot in an encrypted off-host backup. [images.lock.json](images.lock.json) records image versions for recovery; custom builds also need their source or saved image.
