# Gluetun / Proton VPN

A VPN gateway for selected containers.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Requires /dev/net/tun and NET_ADMIN on the Docker host.
- Set supported provider settings and provider-issued OpenVPN credentials.
- Use this gateway or the one included with qBittorrent; avoid duplicate port bindings.

[VPN provider settings](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers) · [Combined media example](../examples/media-stack/README.md)
