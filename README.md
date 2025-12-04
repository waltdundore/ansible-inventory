# ansible-inventory

Environment-specific host definitions for ansible-control project.

## Repository Dependencies

**This repository is part of a three-repository system:**

1. **[ansible-control](https://github.com/waltdundore/ansible-control)** - Main playbooks and roles
2. **THIS REPO** - Environment-specific host definitions
3. **[ansible-config](https://github.com/waltdundore/ansible-config)** - Central configuration file

### Setup

```bash
# Clone all three repositories
cd ~/git
git clone git@github.com:waltdundore/ansible-control.git
git clone git@github.com:waltdundore/ansible-inventory.git
git clone git@github.com:waltdundore/ansible-config.git

# Create symlinks in ansible-control
cd ansible-control
ln -s ../ansible-inventory inventory
ln -s ../ansible-config/config.yml config.yml
```

## Structure

```
ansible-inventory/
├── dev/              # Development environment
│   └── hosts.yml    # Dev hosts (gitignored)
├── prod/            # Production environment
│   ├── hosts.yml    # Prod hosts (gitignored)
│   └── group_vars/  # Production group variables
├── workstation/     # Workstation environment
│   └── hosts.yml    # Workstation hosts (gitignored)
├── hosts.yml.example # Template for creating inventory
└── vagrant.py       # Dynamic inventory for Vagrant VMs
```

## Usage

### Creating Inventory Files

1. Copy the example to your environment:
```bash
cp hosts.yml.example dev/hosts.yml
```

2. Edit and replace:
   - `your_username` with your SSH username
   - Example hostnames with your actual hosts

3. Inventory files are gitignored (environment-specific)

### Inventory Groups

- **vagrant**: Local Vagrant VMs (auto-detected)
- **x86**: Standard x86_64 servers and workstations
- **rpi4**: Raspberry Pi 4 devices
- **rpi5**: Raspberry Pi 5 devices
- **workstation**: Local workstation (localhost)

## Branch Strategy

All three repositories have matching branches:
- `dev` - Development environment
- `prod` - Production environment
- `workstation` - Workstation setup

**IMPORTANT:** Keep all three repos on the same branch when working.

## Dynamic Inventory

The `vagrant.py` script automatically detects running Vagrant VMs and adds them to the `vagrant` group with local connection.

## Important Notes

- Inventory files (`*/hosts.yml`) are gitignored
- Only example file and group_vars are tracked
- Each environment manages inventory separately
- Must be symlinked into ansible-control to function
