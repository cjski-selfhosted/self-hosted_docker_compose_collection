# Sonarr

Tracks TV series, searches configured indexers and coordinates episode downloads/imports with a download client.

## Before you start

Configure indexers, download-client credentials and a series root folder. The standalone /downloads mount must cover your intended library paths, or add a separate library mount. The combined example supplies a shared /data tree for downloads and media.

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
