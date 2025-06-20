# 🐳 Self-Hosted Docker Compose Collection

A collection of Docker Compose files that I use for hosting various services on my server. Simple deployment, enhanced privacy, full control over your data.

This collection is designed for **home server enthusiasts, self-hosting beginners, and advanced users** looking for a quick, flexible, and efficient way to deploy their favorite services. 🚀

---

## 🚀 Why Use This Collection?

- **Easy Setup:** Quickly deploy services using pre-configured Docker Compose files.
- **Self-Hosted & Private:** Keep your data under your control with local or cloud hosting.
- **Flexible & Expandable:** Easily add new services or modify existing ones.
- **Minimal Configuration:** Each service is designed to be ready-to-use with minimal setup.

---

## 📜 List of Services

Here are some self-hosted services included in this collection, linked to their respective GitHub repositories:

* [AdGuard-Home](https://github.com/AdguardTeam/AdGuardHome) - Network-wide ad blocking and DNS filtering
* [Cloudflare-DDNS](https://github.com/favonia/cloudflare-ddns) - A small, feature-rich, and robust Cloudflare DDNS updater
* [Gluetun](https://github.com/qdm12/gluetun) - OpenVPN + ProtonVPN for secure networking
* [Homarr](https://github.com/homarr-labs/homarr) - Dashboard for self-hosted applications
* [Jackett](https://github.com/linuxserver/docker-jackett) - Torrent tracker management
* [Jellyfin](https://github.com/jellyfin/jellyfin) - Open-source media server
* [Nextcloud](https://github.com/nextcloud/docker) - Access & share your files, calendars, contacts, mail & more from any device, on your terms
* [Nginx Proxy](https://github.com/nginx-proxy/nginx-proxy) - Reverse proxy for self-hosted services (replaced by NPM)
* [Nginx Proxy Manager](https://github.com/NginxProxyManager/nginx-proxy-manager) - Reverse proxy for self-hosted services + WEB UI
* [Overseerr](https://github.com/linuxserver/docker-overseerr) - Managing content requests for your media library
* [Pi-Hole](https://github.com/pi-hole/pi-hole) - Network-wide ad blocker and tracker filter
* [Plex](https://github.com/linuxserver/docker-plex) - Media server for streaming movies and TV series
* [Portainer](https://github.com/portainer/portainer) - Container management platform
* [Proton Bridge](https://github.com/shenxn/protonmail-bridge-docker) - IMAP/SMTP Bridge for ProtonMail
* [Radarr](https://github.com/linuxserver/docker-radarr) - See all your upcoming movies in one convenient location
* [Sonarr](https://github.com/linuxserver/docker-sonarr) - See all your upcoming series in one convenient location
* [Speedtest-Tracker](https://github.com/linuxserver/docker-speedtest-tracker) - Monitor your internet speed with automated tests
* [Traefik](https://github.com/traefik/traefik) - Reverse proxy
* [Vaultwarden](https://github.com/dani-garcia/vaultwarden) - Lightweight Bitwarden server implementation
* [qBittorrent](https://github.com/linuxserver/docker-qbittorrent) - BitTorrent client with web UI

💡 Discover other awesome self-hosted apps at [Awesome-Selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted).

---

## 🛠 How to Use

Deploy services easily using **Docker Compose**:

1️⃣ **Clone the repository:**

```bash
git clone git@github.com:cjski-selfhosted/self-hosted_docker_compose_collection.git
cd self-hosted_docker_compose_collection
```

2️⃣ **Navigate to your desired service directory and deploy:**

```bash
cd <service-name>
docker-compose up -d
```

3️⃣ **Verify your service is running:**

```bash
docker-compose ps
```

🔧 **Customization:**  
Each service has a `docker-compose.yml` file. Modify the configurations as needed before deployment.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Add your Docker Compose file in a clearly named directory.
3. Submit a pull request.

---

## 📄 License

This collection is licensed under the **MIT License**. See [LICENSE](LICENSE) for full details.

---

## ✨ Keywords 

self-hosted, docker compose, home server, self-hosting, privacy, media server, VPN, ad-blocking, reverse proxy, automation
