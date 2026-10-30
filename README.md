# Self-hosted Docker Compose collection

Compose definitions for services I run in my home lab, plus a few reference examples I keep around. The current-use definitions were compared with local Docker metadata and Coolify's deployed configurations on **30 October 2026**.

The public files contain service definitions, not my private server layout. Real paths, domains, credentials and volume names go in an ignored `.env` or local configuration file. Each folder has an `.env.example`; my exact source files, runtime settings and machine-specific values are held in a separate protected configuration snapshot.

[Getting started](GETTING_STARTED.md) · [Networks and grouping](NETWORKING.md) · [Combined media example](examples/media-stack/README.md) · [Backup and recovery](RESTORE.md)

## Service catalogue

Open a service name for its prerequisites, configuration and Compose file. Application/database pairs are kept together. The [scope notes](#scope) cover platform components and custom applications.

| Stack | What it is for |
|---|---|
| [cloudflared](cloudflared/README.md) | Connects local web services to Cloudflare through an outbound tunnel, so a public inbound port-forward is not required for that route. |
| [docuseal](docuseal/README.md) | Hosts forms and document-signing workflows, including preparing documents and collecting signatures in a browser. |
| [ghost](ghost/README.md) | A publishing application with an editor, themes, member features and newsletter tooling. This stack includes its MySQL database. |
| [glances](glances/README.md) | Shows host CPU, memory, disk, process and container resource usage through a monitoring interface. |
| [hermes](hermes/README.md) | Runs Hermes Agent with a browser interface for conversations, tools and configured model providers. |
| [homarr](homarr/README.md) | A customisable home page for self-hosted services, links and supported integrations. |
| [it-tools](it-tools/README.md) | A collection of small browser-based developer tools for common conversion, encoding, formatting and generation tasks. |
| [jackett](jackett/README.md) | Provides a common API for configured indexers so tools such as Sonarr and Radarr can search supported sources. |
| [jellyfin](jellyfin/README.md) | An open-source media server for browsing and streaming your own video, music and other supported media to client devices. |
| [maybe-finance](maybe-finance/README.md) | A self-hosted finance application for tracking accounts and financial activity. This definition includes PostgreSQL. |
| [mysql](mysql/README.md) | A MySQL database server for applications that require a relational data store. It has no browser administration interface by itself. |
| [n8n](n8n/README.md) | Builds workflows that connect APIs, webhooks and services. This stack includes PostgreSQL for persistent workflow state. |
| [nextcloud](nextcloud/README.md) | Provides web-based file access, syncing and sharing, with optional apps for calendars, contacts and collaboration. The stack includes MariaDB. |
| [ntfy](ntfy/README.md) | Receives and delivers notifications through topics, HTTP requests and supported clients. Useful for scripts and service alerts. |
| [odoo](odoo/README.md) | A suite of business applications such as CRM, inventory and invoicing, backed here by PostgreSQL. |
| [open-webui](open-webui/README.md) | Runs a web chat interface alongside an Ollama API for locally served models and configured compatible providers. |
| [overseerr](overseerr/README.md) | Lets users browse and request media for a Plex library, then sends approved requests to configured Sonarr/Radarr services. |
| [pgadmin](pgadmin/README.md) | A browser interface for inspecting and administering PostgreSQL servers you are authorised to access. It is not the database server itself. |
| [pi-hole](pi-hole/README.md) | Filters DNS queries for network-wide ad/tracker blocking and provides DNS administration and query visibility. |
| [plex](plex/README.md) | Organises a personal media library and streams it to Plex apps on supported devices. |
| [portainer](portainer/README.md) | A web interface for viewing containers, logs, volumes, networks and deploying/managing stacks. |
| [postgresql](postgresql/README.md) | A PostgreSQL database server for application storage and SQL workloads. |
| [privatebin](privatebin/README.md) | Shares text through a paste interface that encrypts/decrypts in the browser, with expiration and optional access options. |
| [proton-bridge](proton-bridge/README.md) | Exposes a local IMAP/SMTP bridge so compatible mail clients can work with a supported Proton Mail account. |
| [protonvpn](protonvpn/README.md) | Runs Gluetun as a VPN client/gateway; dependent containers can share its network namespace to route their traffic through the VPN. |
| [qbittorrent](qbittorrent/README.md) | Runs qBittorrent with Gluetun so the download client shares the VPN gateway's network namespace. |
| [radarr](radarr/README.md) | Tracks movie collections, searches configured indexers and coordinates downloads/imports with a download client. It is not a player. |
| [samba](samba/README.md) | Shares host directories over SMB for Windows, Linux and other compatible devices. |
| [selenium](selenium/README.md) | Runs a browser automation endpoint for software/tests that drive a supported browser remotely. |
| [sonarr](sonarr/README.md) | Tracks TV series, searches configured indexers and coordinates episode downloads/imports with a download client. |
| [speedtest-tracker](speedtest-tracker/README.md) | Schedules connection speed tests and displays historical results in a web dashboard. |
| [supabase-postgres](supabase-postgres/README.md) | A PostgreSQL image with Supabase-related extensions/configuration. This folder is the database component, not a complete Supabase platform. |
| [traefik](traefik/README.md) | Routes requests to services by hostname/path and can manage HTTPS certificates through configured ACME resolvers. |
| [uptime-kuma](uptime-kuma/README.md) | Checks configured websites/services and presents uptime history, alerts and optional status pages. |
| [vaultwarden](vaultwarden/README.md) | A lightweight server compatible with Bitwarden clients for storing and syncing a password vault. |
| [watchtower](watchtower/README.md) | Checks selected containers for new images and can recreate them with updated images. |

[Coolify platform and import notes](coolify/README.md)

## Reference examples

These additional definitions were not observed running on the inspected host, but remain available as configurable examples.

| Stack | What it is for |
|---|---|
| [AdGuard Home](adguard/README.md) | Network DNS filtering and ad/tracker blocking. |
| [Cloudflare DDNS](cloudflare-ddns/README.md) | Updates selected DNS records when the connection's public IP changes. |
| [NGINX Proxy](nginx-proxy/README.md) | Reverse-proxies containers using its environment-variable discovery convention. |
| [NGINX Proxy Manager](nginx-proxy-manager/README.md) | Configures reverse-proxy hosts and certificates through a browser interface. |

## Start here

New to Docker? Read [Getting started](GETTING_STARTED.md) before deploying. It covers required tools, host folders, permissions, credentials and how to open a loopback-bound service from another computer.

Want related services together? The [networking and grouping guide](NETWORKING.md) explains shared and separate networks, proxy access and why combining files needs care. The [combined media example](examples/media-stack/README.md) puts Plex, Overseerr, Sonarr, Radarr and VPN-routed qBittorrent in one project. It is an optional example, not a migration of existing services.

## Use one stack

```sh
cd <stack-folder>
cp .env.example .env
# Set real paths, credentials and the intended ports.
docker compose --env-file .env config --quiet
# Run only when you intend to deploy the stack:
docker compose --env-file .env up -d
```

You do not need a domain or reverse proxy just to try a service locally. HTTP examples use loopback bindings for local access. Choose a suitable `BIND_ADDRESS` and unused port for your environment; LAN services such as Samba and browser/monitoring services with host networking are documented in their folders. PostgreSQL services have no host-published database port.

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
