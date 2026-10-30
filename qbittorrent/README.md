# qBittorrent + Gluetun

A download client routed through a VPN gateway.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Set provider-issued VPN credentials and writable download paths.
- qBittorrent shares Gluetun’s network namespace; publish its WebUI port on Gluetun.
- Requires /dev/net/tun and NET_ADMIN on the Docker host.

[VPN provider settings](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers) · [Combined media example](../examples/media-stack/README.md)
