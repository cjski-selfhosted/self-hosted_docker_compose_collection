# Portainer

A web interface for viewing containers, logs, volumes, networks and deploying/managing stacks.

## Before you start

Review the Docker socket mount: control of Docker grants broad control of the host. Prepare persistent Portainer storage, create an administrator and protect its management interface. Avoid having multiple tools redeploy the same stack independently.

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
