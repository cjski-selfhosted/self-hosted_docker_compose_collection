# Qbittorrent

Runs `gluetun`, `qbittorrent`. Set paths, credentials and ports in a local `.env`.

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.

## VPN network ownership

This combines the two observed containers into one Compose project. qBittorrent uses `network_mode: service:gluetun` and waits for Gluetun health. Publish access ports on the Gluetun service, not qBittorrent. Fill the VPN provider's credentials/address/region values in `.env`; example addresses are placeholders.

Use this combined stack OR the standalone `../protonvpn` definition, not both. If the VPN container is recreated, recreate its dependent download container as well so it joins the current network namespace. Check the VPN routing and leak protection for your provider and network before relying on it.
