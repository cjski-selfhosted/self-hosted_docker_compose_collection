# Pgadmin

A browser interface for inspecting and administering PostgreSQL servers you are authorised to access. It is not the database server itself.

## Before you start

Set administrator email/password and persistent configuration. Register the intended PostgreSQL host and credentials after login. Join only its required database network and keep the admin interface private.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

## Run this stack

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

## Coolify deployment

The loopback `ports` entry is for local access when running Compose directly. When Coolify owns routing, remove that entry in the imported definition and configure the domain/internal port in Coolify. The platform generates its own labels and networks. See [the platform notes](../coolify/README.md).

## Configuration notes

- Loopback web port is a public convenience; live routing is owned by Coolify/proxy.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.
