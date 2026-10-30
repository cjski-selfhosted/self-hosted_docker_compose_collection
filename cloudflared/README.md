# Cloudflared

Connects local web services to Cloudflare through an outbound tunnel, so a public inbound port-forward is not required for that route.

## Before you start

Create a tunnel in your Cloudflare account and supply its private token. Configure an origin the tunnel can reach over a shared Docker network or an appropriate host route. Add an access policy for private tools.

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
