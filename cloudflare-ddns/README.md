# cloudflare-ddns

Updates selected Cloudflare DNS records when your public IP address changes. Useful for a home connection without a fixed public IP.

## Before you start

You need a Cloudflare-managed zone, selected records and an API token with only the necessary DNS permissions. This updates DNS; it does not open router ports or bypass carrier-grade NAT.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

Reference definition retained from the collection. No matching running container was observed on the inspected Docker host on 30 October 2026; that is not a claim about other machines or future use.

Host paths and environment values are parameterised. Copy `.env.example` to an ignored `.env`, configure it, and validate with `docker compose --env-file .env config --quiet` before choosing to deploy. See [RESTORE.md](../RESTORE.md).
