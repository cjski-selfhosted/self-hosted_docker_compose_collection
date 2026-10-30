# Hermes

Runs `hermes-agent`, `hermes-webui`. Set paths, credentials and ports in a local `.env`.

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

## Configuration notes

- Loopback web port is a public convenience; live routing is owned by Coolify/proxy.
- Public Hermes healthcheck uses the API; private operator bootstrap/configuration is captured separately.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.

## Shared state and API connection

Both containers share the workspace and Hermes state volumes. The agent code volume is mounted read-only in the WebUI. Keep these mappings aligned; changing only one container can produce missing-session/workspace errors.

Set one private `HERMES_API_KEY`: the API server and WebUI gateway use the same value. Provider keys can stay empty for providers you do not use. The public core uses the built-in API `/health` endpoint; private operator bootstrap, local extensions and personalised configuration are restored separately from the protected snapshot. The runtime image references are pinned to the images observed in the snapshot. They do not include later modifications to persistent code/state volumes.

For recovery, restore the existing shared volumes/configuration before starting. For a fresh installation, initialise Hermes and configure providers/workspaces using the upstream setup flow. This repository does not publish private profiles or automation credentials.
