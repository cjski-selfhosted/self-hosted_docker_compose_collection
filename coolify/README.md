# Coolify

A deployment platform for source builds, applications and Compose stacks.

To use a definition here, import its Compose file and configure the variables from its `.env.example`. Set the domain and internal application port in Coolify; remove standalone web port bindings if the proxy handles access.

Coolify manages its own proxy, labels and networks. Keep one deployment owner per stack and one proxy on ports 80/443.

[Coolify documentation](https://coolify.io/docs/start-with-self-hosted)
