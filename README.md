# ansible-inventory

Host definitions for ansible-control. Defines which servers to configure and which roles they get.

## What This Repository Does

Stores the list of servers/hosts for each environment:
- **dev** - Development/testing servers
- **prod** - Production servers
- **workstation** - Local machine

## Setup

**Don't clone this repo alone** - Use the setup script in ansible-control:

```bash
cd ~/git/ansible-control
./setup.sh
```

## Assigning Roles to Hosts

Roles are assigned by **group membership**:

```yaml
---
all:
  vars:
    ansible_user: your_username

  children:
    x86:
      children:
        docker:              # Hosts here get Docker role
          hosts:
            server1.example.com:
            server2.example.com:
        nfs:                 # Hosts here get NFS role
          hosts:
            storage.example.com:
```

**Available role groups:**
- `docker` - Installs Docker engine
- `nfs` - Configures NFS client
- All hosts automatically get `common` role

**Multiple roles:**
```yaml
docker:
  hosts:
    server1.example.com:
nfs:
  hosts:
    server1.example.com:  # Gets both docker and nfs roles
```

## Editing Inventory

```bash
cd ~/git/ansible-inventory
git checkout dev
cd dev
cp hosts.yml.example hosts.yml
nano hosts.yml
```

**What to change:**
- `ansible_user` - Your SSH username
- `server1.example.com` - Your actual hostnames/IPs
- Group membership - Which roles each host gets

## File Structure

```
ansible-inventory/
├── dev/
│   ├── hosts.yml.example    # Template
│   └── hosts.yml            # Your hosts (gitignored)
├── prod/
│   ├── hosts.yml.example
│   └── hosts.yml            # Your hosts (gitignored)
└── workstation/
    ├── hosts.yml.example
    └── hosts.yml            # Your hosts (gitignored)
```

## Why Are hosts.yml Files Gitignored?

Your inventory files contain:
- Server hostnames/IPs
- Usernames
- Environment-specific information

These are **private** and should not be committed to git.

## Branches

- **dev** - Development environment hosts
- **prod** - Production environment hosts
- **workstation** - Local workstation configuration

Switch branches to change environments:
```bash
git checkout prod
```

Or use the setup script in ansible-control:
```bash
cd ~/git/ansible-control
./setup.sh  # Select environment
```

## Usage

This repo is used via symlink from ansible-control:

```bash
cd ~/git/ansible-control
ln -s ../ansible-inventory/dev inventory
make deploy  # Uses inventory/dev/hosts.yml
```

## Getting Help

See ansible-control README and SETUP.md for complete instructions.
