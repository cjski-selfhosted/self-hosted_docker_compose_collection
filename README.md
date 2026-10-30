# Self-hosted Docker Compose collection

Compose definitions for services I run in my home lab, plus a few reference examples I keep around. The current-use definitions were compared with local Docker metadata and Coolify's deployed configurations on **30 October 2026**.

The public files contain service definitions, not my private server layout. Real paths, domains, credentials and volume names go in an ignored `.env` or local configuration file. Each folder has an `.env.example`; my exact source files, runtime settings and machine-specific values are held in a separate protected configuration snapshot.

## Current-use definitions

Related application/database containers stay together. Platform-managed components and custom applications are covered by the [scope notes](#scope), rather than copied out as misleading standalone services.

| Definition | Included services | Observed management |
|---|---|---|
| [cloudflared](cloudflared/docker-compose.yaml) | `cloudflared-admin` | Docker/Portainer or operator Compose |
| [docuseal](docuseal/docker-compose.yaml) | `docuseal` | Coolify |
| [ghost](ghost/docker-compose.yaml) | `mysql`, `ghost` | Coolify |
| [glances](glances/docker-compose.yaml) | `glances` | Coolify |
| [hermes](hermes/docker-compose.yaml) | `hermes-agent`, `hermes-webui` | Docker/Portainer or operator Compose |
| [homarr](homarr/docker-compose.yaml) | `homarr` | Docker/Portainer or operator Compose |
| [it-tools](it-tools/docker-compose.yaml) | `it-tools` | Coolify |
| [jackett](jackett/docker-compose.yaml) | `jackett` | Docker/Portainer or operator Compose |
| [jellyfin](jellyfin/docker-compose.yaml) | `jellyfin` | Docker/Portainer or operator Compose |
| [maybe-finance](maybe-finance/docker-compose.yaml) | `postgres`, `maybe` | Coolify |
| [mysql](mysql/docker-compose.yaml) | `mysql` | Coolify |
| [n8n](n8n/docker-compose.yaml) | `n8n`, `postgresql` | Coolify |
| [nextcloud](nextcloud/docker-compose.yaml) | `nextcloud`, `db` | Docker/Portainer or operator Compose |
| [ntfy](ntfy/docker-compose.yaml) | `ntfy` | Coolify |
| [odoo](odoo/docker-compose.yaml) | `odoo`, `postgresql` | Coolify |
| [open-webui](open-webui/docker-compose.yaml) | `open-webui`, `ollama-api` | Coolify |
| [overseerr](overseerr/docker-compose.yaml) | `overseerr` | Docker/Portainer or operator Compose |
| [pgadmin](pgadmin/docker-compose.yaml) | `pgadmin` | Coolify |
| [pi-hole](pi-hole/docker-compose.yaml) | `pihole` | Docker/Portainer or operator Compose |
| [plex](plex/docker-compose.yaml) | `plex` | Docker/Portainer or operator Compose |
| [portainer](portainer/docker-compose.yaml) | `portainer` | Docker/Portainer or operator Compose |
| [postgresql](postgresql/docker-compose.yaml) | `postgresql` | Coolify |
| [privatebin](privatebin/docker-compose.yaml) | `privatebin` | Coolify |
| [proton-bridge](proton-bridge/docker-compose.yaml) | `protonmail-bridge` | Docker/Portainer or operator Compose |
| [protonvpn](protonvpn/docker-compose.yaml) | `gluetun` | Docker/Portainer or operator Compose |
| [qbittorrent](qbittorrent/docker-compose.yaml) | `gluetun`, `qbittorrent` | Docker/Portainer or operator Compose |
| [radarr](radarr/docker-compose.yaml) | `radarr` | Docker/Portainer or operator Compose |
| [samba](samba/docker-compose.yaml) | `samba` | Docker/Portainer or operator Compose |
| [selenium](selenium/docker-compose.yaml) | `selenium` | Docker/Portainer or operator Compose |
| [sonarr](sonarr/docker-compose.yaml) | `sonarr` | Docker/Portainer or operator Compose |
| [speedtest-tracker](speedtest-tracker/docker-compose.yaml) | `speedtest-tracker` | Docker/Portainer or operator Compose |
| [supabase-postgres](supabase-postgres/docker-compose.yaml) | `postgresql` | Coolify |
| [uptime-kuma](uptime-kuma/docker-compose.yaml) | `uptime-kuma` | Coolify |
| [vaultwarden](vaultwarden/docker-compose.yaml) | `vaultwarden` | Docker/Portainer or operator Compose |
| [watchtower](watchtower/docker-compose.yaml) | `watchtower` | Docker/Portainer or operator Compose |
| [Traefik](traefik/docker-compose.yaml) | Proxy definition and sanitised static configuration example | Coolify owns the live proxy |

[Coolify platform and import notes](coolify/README.md)

## Reference examples

These definitions are retained and parameterised, but were not observed running on the inspected host: [AdGuard](adguard/docker-compose.yaml), [Cloudflare DDNS](cloudflare-ddns/docker-compose.yaml), [NGINX Proxy](nginx-proxy/docker-compose.yaml), and [NGINX Proxy Manager](nginx-proxy-manager/docker-compose.yaml).

## Use one stack

```sh
cd <stack-folder>
cp .env.example .env
# Set real paths, credentials and the intended ports.
docker compose --env-file .env config --quiet
# Run only when you intend to deploy the stack:
docker compose --env-file .env up -d
```

HTTP examples use loopback bindings for local access. Choose a suitable `BIND_ADDRESS` and unused port for your environment; LAN services such as Samba and browser/monitoring services with host networking are documented in their folders. PostgreSQL services have no host-published database port.

If Coolify will own routing, follow [its import notes](coolify/README.md) instead of starting an additional stack beside an existing managed service. The standalone Traefik reference must not compete with Coolify's current proxy for ports 80/443.

## Public definitions and private recovery settings

- **In Git:** Compose files, configuration examples, `.env.example`, and operating notes.
- **Outside Git:** real `.env` files, local overrides, private domains/certificates, account configuration and a runtime/source-file snapshot.
- **Separately retained:** application data and database backups.

The named-volume variables let a recovery use the original volume identities. Do not generate new encryption keys for data that needs its original keys. The [restore guide](RESTORE.md) explains the order and snapshot tool. [images.lock.json](images.lock.json) records the image identities observed with the current-use definitions for version recovery.

## Validate without deployment

```sh
python3 tools/validate_collection.py
python3 -m unittest discover -s tests -v
```

The validator resolves the example Compose files, including the optional GPU combination, checks public-file boundaries and rejects host-published PostgreSQL ports. It does not pull images, start containers, migrate databases or certify an application's restore/health.

## Scope

The inspected estate also contains Coolify's own database/Redis/realtime/sentinel components, custom application images, and private configuration. Those are not interchangeable app templates: recover the platform through its own installation/recovery path and recover custom applications from their source/builds and protected configuration. Private application identifiers, security-camera configuration and automation credentials are not published here.

The Open WebUI/Ollama definition covers the local Docker service. Remote workstation/router configuration and Home Assistant YAML are not part of this collection. Public configuration defaults remove machine-specific values and add documented loopback access where the live service is routed by Coolify; the protected snapshot preserves the exact original settings.
