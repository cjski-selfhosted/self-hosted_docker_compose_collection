# nginx-proxy

Routes HTTP requests to containers using the nginx-proxy environment-variable convention. Useful for consolidating several web services behind one entry point.

## Before you start

Plan ownership of ports 80/443 and a network shared with the intended backends. Container discovery needs Docker socket access. HTTPS certificate automation needs additional configuration; do not run competing proxies on the same host ports.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

Reference definition retained from the collection. No matching running container was observed on the inspected Docker host on 30 October 2026; that is not a claim about other machines or future use.

Host paths and environment values are parameterised. Copy `.env.example` to an ignored `.env`, configure it, and validate with `docker compose --env-file .env config --quiet` before choosing to deploy. See [RESTORE.md](../RESTORE.md).
