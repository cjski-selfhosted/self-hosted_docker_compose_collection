# Combined media stack

One Compose project for Plex, Overseerr, Sonarr, Radarr and qBittorrent/Gluetun, with a shared media network and consistent storage paths.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../../README.md#usage)

## Connections

| Application | Connection or path |
|---|---|
| Overseerr | Plex `plex:32400`, Sonarr `sonarr:8989`, Radarr `radarr:7878` |
| Sonarr / Radarr | qBittorrent at `gluetun:8080`, with its WebUI credentials |
| qBittorrent | Downloads in `/data/downloads` |
| Sonarr | Series in `/data/media/tv` |
| Radarr | Films in `/data/media/movies` |
| Plex | Libraries at `/media/tv` and `/media/movies` |

Set the matching API keys and paths in each application. Only qBittorrent uses the VPN; the other services use the regular bridge. Gluetun needs provider-issued OpenVPN credentials, `/dev/net/tun` and `NET_ADMIN` on the Docker host. [Provider options](https://github.com/qdm12/gluetun-wiki/tree/main/setup/providers).

The default host folders are `./config/<service>` and `./data`, with separate `downloads`, `media/tv` and `media/movies` directories. Create them with suitable permissions, or choose your own paths in `.env`. Plex reads the finished media read-only. Web ports default to localhost.

This is an alternative to the individual stacks; avoid running duplicate applications against the same configuration storage.
