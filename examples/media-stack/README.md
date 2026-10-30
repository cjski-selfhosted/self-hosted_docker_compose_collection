# One combined media project

An optional starting point for a **new** deployment of Plex, Overseerr, Sonarr, Radarr and VPN-routed qBittorrent. It has one Compose file, one `.env` and a project-scoped `media` bridge network. It does not change or reproduce the existing individual stacks on my server.

## What each service does

| Service | Job |
|---|---|
| Plex | Browses and streams the finished media library. |
| Overseerr | Receives requests and sends approved ones to the configured series/movie manager. |
| Sonarr | Manages series, talks to indexers/download client, and imports completed episodes. |
| Radarr | Does the equivalent for films. |
| qBittorrent | Handles authorised downloads. It shares Gluetun's network namespace. |
| Gluetun | Connects to the chosen VPN provider and supplies the downloader's network endpoint. |

## Requirements

- Linux Docker host with Compose, `/dev/net/tun` and permission for the gateway's `NET_ADMIN` capability.
- Enough storage for configuration, incomplete downloads and the finished library; a backup plan for state you care about.
- Correct writable UID/GID for Sonarr, Radarr and qBittorrent. Plex gets read-only access to finished media.
- A supported VPN-provider account and its **OpenVPN service credentials**, which can differ from your normal account login. The example selects Proton VPN; follow [Gluetun's provider instructions](https://github.com/qdm12/gluetun-wiki/blob/main/setup/providers/protonvpn.md). Server selection/features depend on provider/plan. This example does not enable VPN port forwarding.
- A Plex account and any claim/setup step it requires; indexer access and application API keys are configured after startup.

## Prepare and validate

Read [Getting started](../../GETTING_STARTED.md) first. From this folder:

```sh
cp .env.example .env
id -u
id -g
mkdir -p config/{plex,overseerr,sonarr,radarr,qbittorrent,gluetun}
mkdir -p data/downloads data/media/{movies,tv}
# Edit .env: set credentials, UID/GID, paths, timezone and access address.
docker compose --env-file .env config --quiet
# Start only after reviewing storage, permissions and VPN settings:
docker compose --env-file .env up -d
docker compose ps
```

The directory creation commands use Bash brace expansion and assume the example `./config`/`./data` paths. If you change them, prepare those selected locations instead. Don't recursively change ownership of an existing media library without reviewing its current users/permissions.

Ports default to host loopback. For another computer, use an SSH tunnel, deliberate LAN binding or a configured reverse proxy as described in [Getting started](../../GETTING_STARTED.md#4-choose-how-you-will-access-the-service). This bridge example publishes Plex's web port; automatic LAN discovery and remote streaming can need additional Plex configuration. It does not enable hardware transcoding.

## Wire the applications together

Enter these addresses **inside application settings**, not into your laptop browser:

| Caller | Target setting |
|---|---|
| Overseerr | Plex at `http://plex:32400`, Sonarr at `http://sonarr:8989`, Radarr at `http://radarr:7878`; supply the relevant auth/API keys. |
| Sonarr and Radarr | qBittorrent host `gluetun`, port `8080`, configured WebUI credentials. |
| qBittorrent | Download location `/data/downloads` (configure in its settings). |
| Sonarr | Series root `/data/media/tv`. |
| Radarr | Film root `/data/media/movies`. |
| Plex | Film library `/media/movies`, series library `/media/tv`. |

Set up indexers separately in Sonarr/Radarr, or add a selected indexer manager with its own settings. qBittorrent's initial temporary password can be in its startup logs; set a private password before connecting other apps. Gluetun owns its network interface and published WebUI port, so `qbittorrent:8080` is not the target in this layout. Keep `FIREWALL_INPUT_PORTS` aligned with the internal WebUI port if you change it.

Sonarr, Radarr and qBittorrent share the same host data tree at `/data`, avoiding incompatible download paths. Hardlink/atomic-move behaviour also depends on the underlying filesystem and permissions; using the same path alone is not proof that hardlinks work. Do not copy the standalone `/recycle` or `/downloads` mappings into this example without updating the application's paths.

## Check before relying on it

Confirm gateway health, verify the downloader's outbound address through the VPN, and test your intended VPN failure behaviour. Check an actual authorised request/download/import/playback flow with a small permitted item. Health/dependency configuration and successful Compose parsing are not a runtime leak test. API connections, accounts and libraries are not preconfigured by this file.

Only qBittorrent uses the VPN namespace. Other apps use the normal bridge for external API access. No databases, Docker socket, public proxy or watchtower updater are added to this example. For separate projects, a proxy connection or more isolation, see [Networks and combining services](../../NETWORKING.md).
