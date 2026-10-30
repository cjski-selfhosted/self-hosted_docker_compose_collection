# Samba

Shares host directories over SMB for Windows, Linux and other compatible devices.

## Before you start

Use a Linux host, writable source directories and suitable local/network permissions. Prepare config.yml from the provided example, replace account passwords and align share paths with mounts. Host networking uses the host's SMB ports; check for an existing Samba server.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

## Run this stack

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
