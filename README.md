# ansible-inventory

Host definitions for ansible-control. Defines which servers to configure.

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

## Manual Setup (if needed)

```bash
cd ~/git/ansible-inventory
git checkout dev  # or prod, or workstation

# Create inventory file
cd dev
cp hosts.yml.example hosts.yml
nano hosts.yml  # Edit with your hosts
```

## Editing Inventory

**Example inventory file:**
```yaml
---
all:
  vars:
    ansible_connection: ssh
    ansible_user: your_username  # ← Your SSH username
  children:
    x86:
      hosts:
        server1.example.com:     # ← Your server
        server2.example.com:     # ← Add more servers
    rpi4:
      hosts:
        pi1.example.com:         # ← Raspberry Pi hosts
```

**What to change:**
- `ansible_user` - Your SSH username on the servers
- `server1.example.com` - Replace with your actual hostnames or IP addresses

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
