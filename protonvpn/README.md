# Protonvpn

Runs Gluetun as a VPN client/gateway; dependent containers can share its network namespace to route their traffic through the VPN.

## Before you start

Linux /dev/net/tun and NET_ADMIN are required. Supply provider-specific OpenVPN credentials and a supported VPN_SERVICE_PROVIDER. Port forwarding depends on your provider/plan. Use this OR the Gluetun included with qbittorrent, not both on the same ports.

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
