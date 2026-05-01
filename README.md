# homelab-learning

Ansible automation project for managing a Raspberry Pi 5 homelab.

Built as a hands-on learning project to practice real infrastructure automation skills.

## Infrastructure

- **Target host:** Raspberry Pi 5 — 8GB RAM, 512GB M.2 SSD
- **OS:** Raspberry Pi OS Lite (headless)
- **Automation:** Ansible (control node on WSL)
- **Connection:** SSH with key-based authentication

## Project Structure

```
ansible/
├── inventory.ini         # host definitions and SSH config
├── playbook.yml          # main playbook — runs all roles in order
├── group_vars/
│   └── pi.yml            # variables and vault-encrypted secrets
└── roles/
    ├── base/             # creates base folder structure on the Pi
    ├── tools/            # installs common tools (htop, curl, git)
    ├── tmux/             # installs tmux + deploys custom config
    ├── info/             # generates a Pi info file using variables
    ├── system/           # deploys a Jinja2 template with system facts
    ├── conditionals/     # demonstrates conditionals and Ansible Vault
    └── report/           # generates a full system report via template
```

## Concepts Covered

- Inventory and host groups
- Playbooks and roles
- Variables and `group_vars`
- Handlers
- Files and templates (Jinja2)
- Conditionals (`when`)
- Loops
- Tags
- Ansible Vault (encrypted secrets)

## Usage

1. Clone the repo
2. Edit `inventory.ini` with your host IP and SSH user
3. Edit `group_vars/pi.yml` with your variables
4. Encrypt your secrets: `ansible-vault encrypt_string 'your_password' --name 'db_password'`
5. Run the playbook: `ansible-playbook -i inventory.ini playbook.yml --ask-vault-pass`

## Part of a larger homelab

This project is part of a broader homelab running 25+ Docker containers on a Raspberry Pi 5, including monitoring (Grafana + Prometheus), self-hosted cloud (Nextcloud), VPN (WireGuard), and custom Django applications.