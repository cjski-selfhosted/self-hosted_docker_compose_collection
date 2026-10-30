# Open WebUI + Ollama

A web chat interface with local model serving.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Open WebUI connects to ollama-api:11434 on the project network.
- Create an administrator and select/download models after startup.
- The optional AMD/Vulkan override uses /dev/dri and /dev/kfd.

Optional GPU configuration:

```sh
docker compose --env-file .env -f docker-compose.yaml -f docker-compose.gpu.yaml up -d
```
