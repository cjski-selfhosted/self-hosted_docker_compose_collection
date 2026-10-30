# Glances

Shows host CPU, memory, disk, process and container resource usage through a monitoring interface.

## Before you start

This definition requests broad host visibility. Read its mounts, host namespaces and capabilities before deployment. Keep the monitoring interface private and mount the Docker socket read-only where supported; socket access is still sensitive.

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

## Host monitoring

The observed setup uses host PID visibility, privileged monitoring and Docker/Podman socket mounts. Configure only the sockets available on your machine. These permissions are intentional monitoring capabilities; the web endpoint defaults to loopback in this public example.
