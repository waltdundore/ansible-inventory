# ansible-inventory

Host definitions and role assignments for ansible-control.

## Setup

Use ansible-control setup script:

```bash
cd ~/git/ansible-control
./setup.sh
```

## Assign Roles

Edit `hosts.yml` and place hosts in role groups:

```yaml
all:
  vars:
    ansible_user: your_username
  children:
    docker:              # Gets Docker role
      hosts:
        server1.example.com:
    nfs:                 # Gets NFS role
      hosts:
        storage.example.com:
```

**Available role groups:**
- `docker` - Docker engine
- `nfs` - NFS client
- All hosts get `common` role automatically

**Multiple roles:**
```yaml
docker:
  hosts:
    server1.example.com:
nfs:
  hosts:
    server1.example.com:  # Gets both roles
```

## Branches

- `dev` - Development hosts
- `prod` - Production hosts
- `workstation` - Local machine

## Files

- `*/hosts.yml.example` - Template (tracked in git)
- `*/hosts.yml` - Your hosts (gitignored)
