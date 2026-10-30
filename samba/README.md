# Samba

SMB file shares for computers and compatible devices.

[Compose file](docker-compose.yaml) · [Environment settings](.env.example) · [Usage](../README.md#usage)

## Configuration

- Copy config.yml.example to config.yml in the SAMBA_BIND_1 directory.
- Replace account passwords and match share paths to SAMBA_SHARE_*_TARGET.
- Uses host networking and the host’s SMB ports.
