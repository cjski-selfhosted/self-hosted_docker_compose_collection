# Selenium

Runs `selenium`. Set paths, credentials and ports in a local `.env`.

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
