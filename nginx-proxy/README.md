# NGINX Proxy

Automatic reverse proxy using container environment variables.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Share a network with backends and configure their VIRTUAL_HOST/internal port.
- Choose one proxy to own ports 80/443.
