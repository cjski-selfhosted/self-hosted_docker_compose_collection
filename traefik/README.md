# Traefik proxy configuration

The running proxy uses Traefik v3.7 and is owned by Coolify. This public definition preserves its image, Docker/file-provider approach, entrypoint names and DNS-challenge resolver types while removing private domains, credentials, administrative bindings and dynamic backend routes. The exact deployed definition and private files are in the configuration snapshot.

**Do not start this alongside the existing Coolify proxy.** Use it on the intended recovery/standalone host, or restore the existing platform-owned proxy through its controller.

## Prepare local configuration

```sh
cp .env.example .env
mkdir -p config dynamic acme certs
chmod 700 acme
cp traefik.yml.example config/traefik.yml
```

Edit the copied configuration's example domains, email and resolver settings. The observed `letsencrypt` resolver uses DuckDNS; `cflare` uses Cloudflare. Set the corresponding tokens privately in `.env`. Do not put real certificates, ACME state, auth files or backend routes into Git.

The entrypoints are `web` (80), `websecure` (443), `web-tunnel` (8081) and `web-tunnel-secure` (8443). The tunnel entrypoint host bindings default to loopback. The public definition does not publish the administration API port. Put your selected dynamic configuration in the ignored `dynamic` directory, and retain any private certificate files the recovered configuration references.

The `coolify` Docker network is external: use the existing platform network or create the intended network on a new standalone host before deployment. Application routers must attach to a network the proxy can reach and use these entrypoint/resolver names. Coolify normally creates the application routing configuration for its own services.

```sh
docker compose --env-file .env config --quiet
# Deploy only when proxy ownership, ports, DNS and private settings are ready:
docker compose --env-file .env up -d
```

See [the configuration recovery guide](../RESTORE.md). The example file is not a backup of private certificates or a complete export of server-specific routes.
