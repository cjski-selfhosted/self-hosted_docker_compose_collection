# Getting started

Start with one service you want to use. These are configurable examples, not an installer that makes every application ready at once. Each service README explains its purpose and additional requirements.

## 1. Prepare a host

Use a Linux machine or VM with persistent disk space and a working network connection. The Linux-specific stacks (host networking, `/dev/net/tun`, GPU devices and host monitoring) need those features on the Docker host; a Windows/macOS desktop is not a direct replacement for every definition. Check that the selected image supports your CPU architecture. Storage/RAM requirements depend on the application and workload; model serving and media libraries need much more than a small utility.

Install Docker Engine and its Compose plugin using the [official Docker instructions](https://docs.docker.com/engine/install/) and [Compose installation guide](https://docs.docker.com/compose/install/). These commands must work before continuing:

```sh
docker version
docker compose version
docker info
```

Use the current `docker compose` command. If Docker reports a socket permission error, fix access using the installation guide; do not make the socket world-writable. Docker administration grants broad host control. Python 3 is needed only for this repository's validation/backup helpers; Git is needed for cloning/updating the collection.

## 2. Get the files

HTTPS cloning does not require a GitHub SSH key:

```sh
git clone https://github.com/cjski-selfhosted/self-hosted_docker_compose_collection.git
cd self-hosted_docker_compose_collection
cd privatebin  # choose the service you want
cp .env.example .env
```

Read that folder's README and edit `.env` in your editor. Replace `CHANGE_ME` values, choose the storage location and set the access/port values. Keep `.env` private. Some services need a provider account, DNS credentials, an encryption key or additional configuration files; those prerequisites are listed per service. Random application secrets and provider-issued credentials are different: generate your own application secret where supported, but obtain VPN/API credentials from the actual provider.

## 3. Understand the storage paths

A bind mount has a host source and a container destination:

```yaml
volumes:
  - ${MY_CONFIG_DIR}:/config
```

`MY_CONFIG_DIR` selects a directory on the Docker host; `/config` is where this particular container expects it. A variable such as `PLEX_BIND_1` is a host directory, not a password. Read its corresponding mount in the Compose file. Keep expected container destinations intact unless you also change application settings.

`./data/...` paths are relative to the Compose project location. For a permanent setup, consider an absolute directory on the intended disk, such as `/srv/selfhosted/privatebin`. Create required directories and set ownership for the container's user before starting. Check your Linux user/group with:

```sh
id -u
id -g
```

Set `PUID`/`PGID` where the image supports them. Other images use their own user; follow their documentation instead of applying one UID to everything. Avoid `chmod 777` as a general fix. A path intended to be a file (for example Samba's `config.yml` or Traefik's static configuration) must be prepared as a file before deployment. The service README describes those cases.

Named volumes are Docker-managed storage. `VOLUME_*_NAME` variables select their names. For an existing installation, use the original volume identities and matching keys; a new volume name creates different state. See [RESTORE.md](RESTORE.md).

## 4. Choose how you will access the service

Most web examples default to `BIND_ADDRESS=127.0.0.1`. That means the service is accessible on the Docker host, not automatically from your laptop.

For a private first test, use SSH forwarding from your computer, substituting the selected host port:

```sh
ssh -L 8088:127.0.0.1:8088 user@your-server
# Open http://127.0.0.1:8088 on your computer while SSH stays connected.
```

For LAN access, set `BIND_ADDRESS` to the server's intended LAN IP and use that address/port in your browser. `0.0.0.0` listens on all IPv4 interfaces, which can expose more than the LAN. Review router port forwarding and Docker's firewall behaviour before choosing it. Host-networked services do not use Compose port mappings; see [NETWORKING.md](NETWORKING.md).

You do not need a domain or reverse proxy for an initial local web test. Public HTTPS, external webhooks and some applications such as password vaults need further URL/TLS configuration. Pick one routing owner (for example Coolify or a standalone proxy), not two proxies competing for ports 80/443. Never expose a database port just to make two containers communicate.

## 5. Validate, then start deliberately

From the chosen service folder:

```sh
docker compose --env-file .env config --quiet
# When the settings, storage and intended access are ready:
docker compose --env-file .env up -d
docker compose ps
docker compose logs --tail=100
```

`config --quiet` checks Compose configuration without starting anything. It cannot prove provider credentials, disk permissions or application setup are correct. Avoid sharing full resolved `docker compose config` output: it can contain secrets. Logs can also contain temporary credentials or personal information.

Open the selected web port, complete administrator setup and configure integrations. A started container is not proof that email, notifications, backups or another application connection works. Use its actual feature once to check it.

If you need to stop the project, `docker compose down` normally removes its containers and project networks while retaining named volumes. Do not add `-v` when keeping existing data. Updating an application requires checking release notes, matching configuration/data backups and an appropriate rollback or migration plan; an old image alone may not undo a database migration.

## Common first-run problems

| Symptom | Check |
|---|---|
| Docker command cannot connect | Is the daemon running, and does your account have access? |
| Port already allocated | Another service owns that host port; change the host-side port or choose its existing proxy. |
| Browser works on the server only | Loopback binding is intentional; use the SSH tunnel or configure LAN/proxy access. |
| Permission denied on a volume | Check host ownership, expected image UID/GID, and whether the path is a file or directory. |
| Container cannot reach another container | Check shared networks and service names; use the destination's internal port. |
| App starts with an empty library/database | Check whether you selected a new path/volume instead of the intended existing one. |
| VPN gateway stays unhealthy | Check provider credentials, supported country/server selection, `/dev/net/tun` and provider-specific requirements. |

Use the [network guide](NETWORKING.md) for multi-service setups and the [combined media example](examples/media-stack/README.md) for one complete project layout. Configuration recovery and data backups are explained in [RESTORE.md](RESTORE.md).
