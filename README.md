# Inventory Directory

## Purpose

This directory contains environment-specific host definitions and variables. Inventory files define **what hosts exist** and **how to connect to them**.

## Structure

```
inventory/
├── README.md              # This file
├── hosts.yml.example      # Template for creating inventory files
├── vagrant.py             # Dynamic inventory for Vagrant VMs
├── dev/
│   ├── hosts.yml          # Development hosts (gitignored)
│   └── group_vars/        # Dev-specific variables
└── prod/
    ├── hosts.yml          # Production hosts (gitignored)
    └── group_vars/        # Prod-specific variables
```

## Setup Instructions

### 1. Create Your Inventory Files

```bash
# For development environment
cp inventory/hosts.yml.example inventory/dev/hosts.yml

# For production environment
cp inventory/hosts.yml.example inventory/prod/hosts.yml
```

### 2. Edit Inventory Files

Open `inventory/dev/hosts.yml` or `inventory/prod/hosts.yml` and:

1. **Replace `your_username`** with your actual SSH username
2. **Replace example hostnames** with your actual hosts
3. **Add/remove host groups** as needed

### 3. Understanding the Structure

```yaml
all:
  vars:
    ansible_user: your_username  # ← REPLACE THIS with your SSH username
  children:
    x86:
      hosts:
        myserver.example.com:    # ← REPLACE with your actual hostname
```

## Important Concepts

### ansible_user Variable

The `ansible_user` variable you set in inventory is **the only place** where your username should be hardcoded. This value:

- Defines which user Ansible connects as via SSH
- Becomes `{{ ansible_user }}` in playbooks
- Becomes `{{ common_user }}` in roles (via defaults)
- Is used for SSH key deployment and sudo configuration

**Example Flow:**
```
inventory/dev/hosts.yml:
  ansible_user: alice

roles/common/defaults/main.yml:
  common_user: "{{ ansible_user }}"  # Becomes "alice"

roles/common/tasks/ssh_keys.yml:
  user: "{{ common_user }}"          # Deploys key for "alice"
```

### Branch-Based Inventory Selection

The Makefile automatically selects the correct inventory based on your git branch:

- On `dev` branch → uses `inventory/dev/hosts.yml`
- On `prod` branch → uses `inventory/prod/hosts.yml`

This ensures you never accidentally deploy to production while testing.

### Why Inventory Files Are Gitignored

Inventory files contain environment-specific information:
- Usernames (your SSH user)
- Hostnames (your actual servers)
- IP addresses
- Environment-specific settings

These are **personal to your environment** and should not be committed to git. Each user/environment maintains their own inventory files.

## Host Groups

Organize hosts into logical groups:

### vagrant
Local Vagrant VMs for testing. Uses `ansible_connection: local`.

### x86
Standard x86_64 servers and workstations (Fedora, Debian, etc.)

### rpi4
Raspberry Pi 4 devices

### rpi5
Raspberry Pi 5 devices

## Group Variables

Place group-specific variables in `group_vars/`:

```
inventory/dev/group_vars/
├── all.yml          # Variables for all hosts
├── x86.yml          # Variables for x86 group
└── rpi4.yml         # Variables for rpi4 group
```

## Dynamic Inventory

The `vagrant.py` script provides dynamic inventory for Vagrant VMs:
- Automatically detects running Vagrant VMs
- Used by `make provision` for efficiency
- No manual inventory updates needed for Vagrant

## Troubleshooting

### "ansible_user not defined"
Make sure you've set `ansible_user` in your inventory file under `all.vars`.

### "Permission denied (publickey)"
Check that:
1. Your SSH key is deployed to the target host
2. `ansible_user` matches your actual SSH username
3. SSH key path in `config.yml` is correct

### "Host not found"
Verify:
1. Hostname is correct in inventory
2. Host is reachable: `ping hostname.example.com`
3. DNS or `/etc/hosts` is configured

## Best Practices

1. **Keep dev and prod separate** - Never use production hosts in dev inventory
2. **Use descriptive hostnames** - `webserver-01` not `server1`
3. **Document special hosts** - Add comments for hosts with unique configs
4. **Test with Vagrant first** - Always test changes locally before deploying
5. **Backup your inventory** - Keep a secure backup of production inventory

## Example Inventory

See `hosts.yml.example` for a complete, documented example.
