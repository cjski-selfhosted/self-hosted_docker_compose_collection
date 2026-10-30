# Self-hosted Docker Compose collection

Docker Compose files for services I use or have used in my home lab.

## Services

| Service | What it is for |
|---|---|
| [AdGuard Home](adguard/README.md) | Network-wide DNS filtering and ad blocking. |
| [Cloudflare DDNS](cloudflare-ddns/README.md) | Updates Cloudflare DNS records when your public IP changes. |
| [Cloudflare Tunnel](cloudflared/README.md) | Connects local services to Cloudflare through an outbound tunnel. |
| [DocuSeal](docuseal/README.md) | Document forms, filling and electronic signatures. |
| [Ghost](ghost/README.md) | Blog publishing, memberships and newsletters. |
| [Glances](glances/README.md) | Host and container resource monitoring. |
| [Hermes Agent](hermes/README.md) | AI agent runtime with a browser chat interface. |
| [Homarr](homarr/README.md) | A dashboard for self-hosted applications and integrations. |
| [IT Tools](it-tools/README.md) | Browser utilities for encoding, formatting and conversions. |
| [Jackett](jackett/README.md) | Connects supported indexers to media automation tools. |
| [Jellyfin](jellyfin/README.md) | An open-source server for streaming your media library. |
| [Maybe Finance](maybe-finance/README.md) | Personal finance and account tracking. |
| [MySQL](mysql/README.md) | A relational database for applications and SQL workloads. |
| [n8n](n8n/README.md) | Visual workflows connecting APIs, webhooks and applications. |
| [Nextcloud](nextcloud/README.md) | File syncing, sharing and collaboration across devices. |
| [NGINX Proxy](nginx-proxy/README.md) | Automatic reverse proxy using container environment variables. |
| [NGINX Proxy Manager](nginx-proxy-manager/README.md) | Reverse-proxy hosts and HTTPS certificates managed through a web UI. |
| [ntfy](ntfy/README.md) | Push notifications from scripts, applications and HTTP requests. |
| [Odoo](odoo/README.md) | Business applications including CRM, inventory and invoicing. |
| [Open WebUI + Ollama](open-webui/README.md) | A web chat interface with local model serving. |
| [Overseerr](overseerr/README.md) | Media requests connected to Plex, Sonarr and Radarr. |
| [pgAdmin](pgadmin/README.md) | A browser interface for managing PostgreSQL databases. |
| [Pi-hole](pi-hole/README.md) | Network-wide DNS filtering and ad/tracker blocking. |
| [Plex](plex/README.md) | Streams your media library to supported devices. |
| [Portainer](portainer/README.md) | A web interface for containers, stacks, volumes and networks. |
| [PostgreSQL](postgresql/README.md) | A relational database for applications and SQL workloads. |
| [PrivateBin](privatebin/README.md) | Encrypted text sharing with expiring pastes. |
| [Proton Mail Bridge](proton-bridge/README.md) | Connects compatible mail clients to Proton Mail through IMAP/SMTP. |
| [Gluetun / Proton VPN](protonvpn/README.md) | A VPN gateway for selected containers. |
| [qBittorrent + Gluetun](qbittorrent/README.md) | A download client routed through a VPN gateway. |
| [Radarr](radarr/README.md) | Movie discovery, downloads and library imports. |
| [Samba](samba/README.md) | SMB file shares for computers and compatible devices. |
| [Selenium](selenium/README.md) | A browser automation endpoint for scripts and tests. |
| [Sonarr](sonarr/README.md) | TV series tracking, downloads and library imports. |
| [Speedtest Tracker](speedtest-tracker/README.md) | Scheduled internet speed tests and historical results. |
| [Supabase PostgreSQL](supabase-postgres/README.md) | PostgreSQL with Supabase-related extensions and configuration. |
| [Traefik](traefik/README.md) | Reverse proxy and automated HTTPS routing for applications. |
| [Uptime Kuma](uptime-kuma/README.md) | Availability checks, alerting and status pages. |
| [Vaultwarden](vaultwarden/README.md) | A lightweight password-vault server compatible with Bitwarden clients. |
| [Watchtower](watchtower/README.md) | Container image checks and automatic updates for selected services. |

[Coolify](coolify/README.md) handles application deployment and can run these stacks too.

## Usage

**Requirement:** Docker with Compose, available on Linux, Windows and macOS.

```sh
git clone https://github.com/cjski-selfhosted/self-hosted_docker_compose_collection.git
cd self-hosted_docker_compose_collection/<service>
cp .env.example .env
# Edit .env with your paths, credentials and ports.
docker compose --env-file .env up -d
```

Each folder contains its Compose file, environment example and service-specific notes. Web ports default to localhost; adjust `BIND_ADDRESS` for LAN access or use a reverse proxy. Keep real credentials and configuration out of Git.

## Grouping services

Related services can share one Compose project or stay in separate projects connected by a shared network. For example, Plex, Sonarr, Radarr, Overseerr and qBittorrent can form one media stack, with only qBittorrent using the VPN gateway.

[Network examples](NETWORKING.md) · [Combined media stack](examples/media-stack/README.md)

## Backup and validation

[Configuration backup and recovery](RESTORE.md) · [Image version record](images.lock.json)

Validate the definitions without starting containers:

```sh
python3 tools/validate_collection.py
```
