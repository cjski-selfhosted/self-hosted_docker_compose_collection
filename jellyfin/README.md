# Jellyfin

An open-source media server for browsing and streaming your own video, music and other supported media to client devices.

## Before you start

Prepare media directories and separate persistent server configuration. Grant read access to media; hardware transcoding requires compatible hardware/device mappings and is not enabled by every template.

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
