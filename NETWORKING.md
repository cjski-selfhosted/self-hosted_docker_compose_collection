# Network examples

Services can be grouped by purpose while keeping unrelated applications on separate networks.

| Layout | Example |
|---|---|
| One project, one network | Plex, Overseerr, Sonarr and Radarr share a media network. |
| Separate projects, shared network | Sonarr and Radarr deploy independently but reach the same download client. |
| Two networks for an application | A web app joins the proxy and database networks; its database stays on the database network. |
| VPN for one service | qBittorrent shares Gluetun’s network namespace; the other media services use the regular bridge. |

## A combined media project

The [media example](examples/media-stack/README.md) contains Plex, Overseerr, Sonarr, Radarr and qBittorrent/Gluetun in one Compose file.

```text
Overseerr → Sonarr / Radarr → qBittorrent via Gluetun
                  ↓
             Media library → Plex
```

Sonarr and Radarr reach the download client at `gluetun:8080`. Shared data paths let them import completed downloads into the library.

## An app on two networks

This fragment illustrates network membership:

```yaml
services:
  app:
    networks: [proxy, database]
  db:
    networks: [database]
networks:
  database: {}
  proxy:
    external: true
    name: shared-proxy
```

The proxy can reach the app without putting the database on its network. An external network is shared across projects and must already exist. Containers on a shared network use service names and internal ports; host-published ports are for access from outside that network.

Combining files also means checking for duplicate service names, ports, variables and volume names. See [Docker’s networking documentation](https://docs.docker.com/compose/how-tos/networking/) for the full options.
