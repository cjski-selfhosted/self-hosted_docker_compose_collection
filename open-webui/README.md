# Open Webui

Runs `open-webui`, `ollama-api`. Set paths, credentials and ports in a local `.env`.

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

- GPU override preserves the observed AMD/Vulkan device configuration; base file runs without GPU devices.
- Loopback web port is a public convenience; live routing is owned by Coolify/proxy.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.

## GPU mode used in the lab

The base file is usable without exposing the model API on the host. Open WebUI reaches `ollama-api:11434` on the stack network. The optional AMD/Vulkan override preserves the observed `/dev/dri` and `/dev/kfd` device setup:

```sh
docker compose --env-file .env -f docker-compose.yaml -f docker-compose.gpu.yaml config --quiet
# Deploy this combination only on a machine with the matching devices:
docker compose --env-file .env -f docker-compose.yaml -f docker-compose.gpu.yaml up -d
```

A separate inference workstation/router is outside this local Docker stack; this definition does not claim to reproduce it.
