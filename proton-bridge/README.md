# Proton Bridge

Exposes a local IMAP/SMTP bridge so compatible mail clients can work with a supported Proton Mail account.

## Before you start

Confirm your Proton plan supports Bridge and complete the image's login/setup flow. Bridge-generated mail credentials differ from account credentials. Keep IMAP/SMTP access private and preserve the account/key storage.

Read the [first-run guide](../GETTING_STARTED.md) for Docker installation, paths, credentials and access, and the [networking guide](../NETWORKING.md) before connecting this stack to other services. The [Compose definition](docker-compose.yaml) and [.env.example](.env.example) are the settings checklist.

## Run this stack

```sh
cp .env.example .env
# Edit .env: set real paths, unique credentials and the intended local port.
docker compose --env-file .env config --quiet
docker compose --env-file .env up -d
```

For recovery, select the original volumes with `VOLUME_*_NAME` and restore their matching encryption/API keys. Keep `.env` and application state out of Git.

See [the restore guide](../RESTORE.md) for the configuration snapshot and recovery order.
