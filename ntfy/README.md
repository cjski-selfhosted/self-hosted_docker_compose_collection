# Ntfy

Receives and delivers notifications through topics, HTTP requests and supported clients. Useful for scripts and service alerts.

## Before you start

Decide which topics are private and configure authentication/authorisation before exposing the server. Set the public base URL and persistent settings/cache as needed. A running server does not automatically subscribe your phone.

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

## Optional integrations

Leave optional SMTP/upstream/web-push settings empty when unused. Replace every non-empty `CHANGE_ME` value before enabling that integration; reuse the original private keys when restoring an existing installation. The service's authentication/access settings are configuration, while its stored messages/users belong to the separately managed state.
