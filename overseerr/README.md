# Overseerr

Lets users browse and request media for a Plex library, then sends approved requests to configured Sonarr/Radarr services.

## Before you start

You need a Plex account/server for this setup and reachable Sonarr/Radarr APIs. Add their API keys in Overseerr and configure request approval rules; Compose networking alone does not connect the applications.

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
