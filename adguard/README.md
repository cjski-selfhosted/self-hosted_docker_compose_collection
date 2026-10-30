# adguard

A DNS server that blocks configured advertising and tracking domains for devices on your network.

## Before you start

Choose a static LAN address and check port 53 is free. Another DNS resolver or systemd-resolved may already own it. Configure clients/router to use this DNS server after testing it; keep a way to restore the previous resolver.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

Reference definition retained from the collection. No matching running container was observed on the inspected Docker host on 30 October 2026; that is not a claim about other machines or future use.

Host paths and environment values are parameterised. Copy `.env.example` to an ignored `.env`, configure it, and validate with `docker compose --env-file .env config --quiet` before choosing to deploy. See [RESTORE.md](../RESTORE.md).
