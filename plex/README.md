# Plex

Organises a personal media library and streams it to Plex apps on supported devices.

## Before you start

Prepare media and persistent configuration directories, plus a Plex account/claim token when needed. Set read permissions for the library. Discovery, remote access and hardware transcoding need their own network/hardware/account setup.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

## Run this stack

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

## Configuration notes

- Loopback web port is a public convenience; live routing is owned by Coolify/proxy.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.
