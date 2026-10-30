# Qbittorrent

Runs qBittorrent with Gluetun so the download client shares the VPN gateway's network namespace.

## Before you start

You need Linux /dev/net/tun, NET_ADMIN and valid VPN-provider credentials. Configure the download paths, WebUI credentials and download-client integrations. The WebUI port is published by Gluetun, not qBittorrent. Use the combined media example for a consistent shared /data layout.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

## VPN credentials and ports

The public example selects `VPN_SERVICE_PROVIDER=protonvpn`; choose a supported provider and follow [Gluetun's provider setup](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers). `OPENVPN_USER` and `OPENVPN_PASSWORD` are credentials issued by the provider, not random secrets to generate yourself. `UPDATER_PROTONVPN_*` are separate optional server-updater settings; configure them only when using that feature. Port forwarding is off in the public environment example; enabling it requires provider/plan support and matching downloader configuration. Publishing a Docker port does not request a forwarded VPN-provider port.

## Run this stack

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
