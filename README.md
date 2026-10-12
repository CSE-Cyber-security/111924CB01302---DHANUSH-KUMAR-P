# Week 01 – Cybersecurity Asset Inventory System

A menu-driven Python program that helps a security administrator **add, search, update, delete and display** an organization's IT assets (workstations, servers, routers, switches and applications), classify them by **risk level** and **security status**, and quickly spot which assets need immediate attention.

## Features
- Add multiple assets in one go
- Display the full inventory with summary counts
- Search by Asset ID, name, type, IP address or department
- Update any field of an existing asset
- Delete an asset (with confirmation)
- Security summary: counts by risk level and status, plus a list of assets needing immediate attention (Critical risk or Vulnerable status)
- Input validation for every field
- Data saved to a JSON file, so it persists between runs

## Repository Structure
```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## Requirements
- Python 3.6 or higher (standard library only – no packages to install)

## How to Run
```bash
git clone <your-repo-url>
cd Week-01-Cybersecurity-Asset-Inventory
python src/asset_inventory.py
```
Optionally pass a different data file: `python src/asset_inventory.py my_assets.json`

## Allowed Values
| Field | Allowed values |
|-------|----------------|
| Asset Type | Workstation, Server, Router, Switch, Application |
| Risk Level | Low, Medium, High, Critical |
| Security Status | Secure, Warning, Vulnerable |

## Input Validation
- Asset ID must be unique, non-empty and contain no spaces
- Asset Type, Risk Level and Security Status must match the allowed values (case-insensitive)
- IP address must be a valid IPv4/IPv6 address
- Name, Operating System and Department cannot be empty
- Number of assets and menu choices must be valid numbers

## Sample Run
Adding the three sample assets, then displaying the inventory, gives:
```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID    : A101
Asset Name  : HR-PC-01
Asset Type  : Workstation
IP Address  : 192.168.1.10
OS          : Windows 11
Department  : HR
Risk Level  : Medium
Status      : Secure
-----------------------------------------
Asset ID    : A102
Asset Name  : Web-Server
Asset Type  : Server
IP Address  : 192.168.1.20
OS          : Ubuntu
Department  : IT
Risk Level  : Critical
Status      : Vulnerable
-----------------------------------------
Asset ID    : A103
Asset Name  : Core-Router
Asset Type  : Router
IP Address  : 192.168.1.1
OS          : Cisco IOS
Department  : Network
Risk Level  : High
Status      : Warning
=========================================
Total Assets        : 3
Critical Assets     : 1
High Risk Assets    : 1
Medium Risk Assets  : 1
Low Risk Assets     : 0
Vulnerable Assets   : 1
=========================================
```

## Screenshots
| Feature | Screenshot |
|---------|-----------|
| Add asset | ![Add](screenshots/01-add-asset.png) |
| Display assets | ![Display](screenshots/02-display-assets.png) |
| Search asset | ![Search](screenshots/03-search-asset.png) |
| Update asset | ![Update](screenshots/04-update-asset.png) |
| Delete asset | ![Delete](screenshots/05-delete-asset.png) |
| Security summary | ![Summary](screenshots/06-security-summary.png) |
| Input validation | ![Validation](screenshots/07-input-validation.png) |

## Testing
20 test cases covering all features and validation rules are documented in [tests/test_cases.md](tests/test_cases.md).

## Push to GitHub
```bash
git init
git add .
git commit -m "Week 01: Cybersecurity Asset Inventory System"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
