# Coolify owns its platform stack

I use Coolify for source builds, application deployments and some service stacks. Its proxy, database, Redis, realtime and sentinel components belong to the platform installation. They are not independent applications to recreate from copied container names.

Use the [official installation and upgrade instructions](https://coolify.io/docs/get-started/installation). For recovery, keep a private copy of the platform's `.env`, installation Compose files, service Compose definitions and environment settings. Preserve the platform's own recovery material separately.

The application folders in this collection contain portable service definitions. To import one into Coolify:

1. Create a Docker Compose service from its definition.
2. Set the variables using that folder's `.env.example` as a checklist.
3. Remove the local-access `ports` block when Coolify will own routing.
4. Set the application's domain and internal port in Coolify, then review storage before deploying.

Coolify generates its own container names, labels and networks. Those generated IDs, private domains and authentication settings are kept in the private configuration snapshot, not committed here. The running Coolify proxy should not be replaced by starting the standalone example in `../traefik`.
