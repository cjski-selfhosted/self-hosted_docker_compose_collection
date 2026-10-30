# Traefik

Reverse proxy and automated HTTPS routing for applications.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Prepare the static/dynamic configuration and ACME storage paths.
- Set DNS-provider tokens privately; edit domains/email in the static config example.
- The external coolify network must exist. Use one proxy to own ports 80/443.
