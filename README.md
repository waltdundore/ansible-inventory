# ansible-inventory

Environment-specific host definitions for ansible-control.

## Branch Structure

- `dev` - Development hosts
- `prod` - Production hosts
- `workstation` - Local workstation

## Setup

```bash
cd ~/git/ansible-inventory
git checkout dev
cp dev/hosts.yml.example dev/hosts.yml
vim dev/hosts.yml
```

Update `ansible_user` and hostnames.

## Usage

Link from ansible-control:

```bash
cd ~/git/ansible-control
ln -s ../ansible-inventory/dev inventory
```

## File Structure

```
dev/hosts.yml          # Dev hosts (gitignored)
prod/hosts.yml         # Prod hosts (gitignored)
workstation/hosts.yml  # Workstation (gitignored)
```
