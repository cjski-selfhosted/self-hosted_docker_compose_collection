# Samba

Runs `samba`. Set paths, credentials and ports in a local `.env`.

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.

## Samba configuration file

The image reads `/data/config.yml`. Copy `config.yml.example` to `config.yml` inside the host directory selected by `SAMBA_BIND_1`. Change the example users/passwords and ensure each share path matches its `SAMBA_SHARE_*_TARGET` mount. The example preserves the share structure while replacing personal account/share names. Your actual file is held in the private configuration snapshot.

Samba uses host networking in the observed setup. Review the host's LAN access rules before deploying.
