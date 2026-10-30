# Selenium

Runs a browser automation endpoint for software/tests that drive a supported browser remotely.

## Before you start

Automation scripts need a compatible WebDriver client and the configured browser image. Read host-networking and shared-memory settings before deployment. Keep the control endpoint private; access can allow remote browser execution.

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

## Browser service

The observed deployment uses host networking and a larger shared-memory allocation. Keep this browser automation endpoint on a trusted local network; this example does not add public authentication or an Internet-facing proxy route.
