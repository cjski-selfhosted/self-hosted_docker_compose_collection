# Open Webui

Runs a web chat interface alongside an Ollama API for locally served models and configured compatible providers.

## Before you start

Allocate disk and RAM for your chosen models, initialise an administrator and download/select a model after startup. The base is usable without GPU acceleration; the optional override requires compatible AMD/Vulkan devices/drivers. This does not deploy a remote llama.cpp workstation.

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
