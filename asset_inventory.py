"""
Cybersecurity Asset Inventory System
------------------------------------
A menu-driven program that lets a security administrator add, search,
update, delete and display IT assets, and classify them by asset type
and security risk level. Data is stored in ../data/assets.json.

Usage:
    python asset_inventory.py                # uses data/assets.json
    python asset_inventory.py my_data.json   # uses a custom data file
"""

import ipaddress
import json
import os
import sys

# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA_FILE = os.path.join(BASE_DIR, "..", "data", "assets.json")
DATA_FILE = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DATA_FILE

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

LINE_DOUBLE = "=" * 41
LINE_SINGLE = "-" * 41


# ----------------------------------------------------------------------
# Input / output helpers
# ----------------------------------------------------------------------
def read(prompt):
    """Read a line of input. Echo it when input is piped (for logs/screenshots)."""
    value = input(prompt).strip()
    if not sys.stdin.isatty():
        print(value)
    return value


def info(message):
    print(f"[+] {message}")


def error(message):
    print(f"[!] {message}")


def ask_text(prompt):
    """Ask for a non-empty text value."""
    while True:
        value = read(prompt)
        if value:
            return value
        error("This field cannot be empty.")


def ask_choice(prompt, options):
    """Ask for a value that must match one of `options` (case-insensitive)."""
    lookup = {o.lower(): o for o in options}
    while True:
        value = read(f"{prompt} ({'/'.join(options)}): ")
        if value.lower() in lookup:
            return lookup[value.lower()]
        error(f"Invalid input. Choose one of: {', '.join(options)}.")


def ask_ip(prompt):
    """Ask for a valid IPv4/IPv6 address."""
    while True:
        value = read(prompt)
        try:
            return str(ipaddress.ip_address(value))
        except ValueError:
            error("Invalid IP address. Example: 192.168.1.10")


def ask_positive_int(prompt):
    """Ask for a positive whole number."""
    while True:
        value = read(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        error("Please enter a whole number greater than 0.")


def ask_asset_id(assets):
    """Ask for a unique Asset ID (no spaces)."""
    while True:
        value = read("Asset ID: ").upper()
        if not value or " " in value:
            error("Asset ID cannot be empty or contain spaces.")
        elif find_by_id(assets, value):
            error(f"Asset ID {value} already exists. Use a unique ID.")
        else:
            return value


# ----------------------------------------------------------------------
# Data storage
# ----------------------------------------------------------------------
def load_assets():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        error("Data file is unreadable. Starting with an empty inventory.")
        return []


def save_assets(assets):
    os.makedirs(os.path.dirname(os.path.abspath(DATA_FILE)), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4)


def find_by_id(assets, asset_id):
    for asset in assets:
        if asset["asset_id"].upper() == asset_id.upper():
            return asset
    return None


# ----------------------------------------------------------------------
# Display helpers
# ----------------------------------------------------------------------
def print_asset(asset):
    print(f"Asset ID    : {asset['asset_id']}")
    print(f"Asset Name  : {asset['asset_name']}")
    print(f"Asset Type  : {asset['asset_type']}")
    print(f"IP Address  : {asset['ip_address']}")
    print(f"OS          : {asset['operating_system']}")
    print(f"Department  : {asset['department']}")
    print(f"Risk Level  : {asset['risk_level']}")
    print(f"Status      : {asset['security_status']}")


def print_menu():
    print()
    print(LINE_DOUBLE)
    print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
    print(LINE_DOUBLE)
    print("1. Add Assets")
    print("2. Display All Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Security Summary")
    print("7. Exit")
    print(LINE_SINGLE)


# ----------------------------------------------------------------------
# Features
# ----------------------------------------------------------------------
def add_assets(assets):
    count = ask_positive_int("Enter number of assets: ")
    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        asset = {
            "asset_id": ask_asset_id(assets),
            "asset_name": ask_text("Asset Name: "),
            "asset_type": ask_choice("Asset Type", ASSET_TYPES),
            "ip_address": ask_ip("IP Address: "),
            "operating_system": ask_text("Operating System: "),
            "department": ask_text("Department: "),
            "risk_level": ask_choice("Risk Level", RISK_LEVELS),
            "security_status": ask_choice("Security Status", SECURITY_STATUSES),
        }
        assets.append(asset)
        save_assets(assets)
        info(f"Asset {asset['asset_id']} added successfully.")


def display_assets(assets):
    print()
    print(LINE_DOUBLE)
    print(" CYBERSECURITY ASSET INVENTORY")
    print(LINE_DOUBLE)
    if not assets:
        print("No assets found.")
        print(LINE_DOUBLE)
        return
    for index, asset in enumerate(assets):
        print_asset(asset)
        print(LINE_SINGLE if index < len(assets) - 1 else LINE_DOUBLE)
    print_summary_counts(assets)


def search_asset(assets):
    keyword = ask_text("Enter Asset ID, Name, Type, IP or Department to search: ").lower()
    matches = [
        a for a in assets
        if any(keyword in str(a[k]).lower()
               for k in ("asset_id", "asset_name", "asset_type", "ip_address", "department"))
    ]
    if not matches:
        error("No matching asset found.")
        return
    info(f"{len(matches)} asset(s) found.")
    print(LINE_SINGLE)
    for asset in matches:
        print_asset(asset)
        print(LINE_SINGLE)


def update_asset(assets):
    asset = find_by_id(assets, ask_text("Enter Asset ID to update: "))
    if not asset:
        error("Asset not found.")
        return
    fields = {
        "1": ("Asset Name", "asset_name"),
        "2": ("Asset Type", "asset_type"),
        "3": ("IP Address", "ip_address"),
        "4": ("Operating System", "operating_system"),
        "5": ("Department", "department"),
        "6": ("Risk Level", "risk_level"),
        "7": ("Security Status", "security_status"),
    }
    while True:
        print("\nWhich field do you want to update?")
        for key, (label, _) in fields.items():
            print(f"{key}. {label}")
        print("0. Done")
        choice = read("Enter choice: ")
        if choice == "0":
            break
        if choice not in fields:
            error("Invalid choice.")
            continue
        label, key = fields[choice]
        if key == "asset_type":
            asset[key] = ask_choice(label, ASSET_TYPES)
        elif key == "risk_level":
            asset[key] = ask_choice(label, RISK_LEVELS)
        elif key == "security_status":
            asset[key] = ask_choice(label, SECURITY_STATUSES)
        elif key == "ip_address":
            asset[key] = ask_ip(f"New {label}: ")
        else:
            asset[key] = ask_text(f"New {label}: ")
        save_assets(assets)
        info(f"{label} updated successfully.")
    print(LINE_SINGLE)
    print_asset(asset)
    print(LINE_SINGLE)


def delete_asset(assets):
    asset = find_by_id(assets, ask_text("Enter Asset ID to delete: "))
    if not asset:
        error("Asset not found.")
        return
    confirm = ask_choice(f"Delete {asset['asset_id']} - {asset['asset_name']}? ", ["yes", "no"])
    if confirm == "yes":
        assets.remove(asset)
        save_assets(assets)
        info(f"Asset {asset['asset_id']} deleted successfully.")
    else:
        info("Delete cancelled.")


def print_summary_counts(assets):
    count = lambda key, val: sum(1 for a in assets if a[key] == val)
    print(f"Total Assets        : {len(assets)}")
    print(f"Critical Assets     : {count('risk_level', 'Critical')}")
    print(f"High Risk Assets    : {count('risk_level', 'High')}")
    print(f"Medium Risk Assets  : {count('risk_level', 'Medium')}")
    print(f"Low Risk Assets     : {count('risk_level', 'Low')}")
    print(f"Vulnerable Assets   : {count('security_status', 'Vulnerable')}")
    print(LINE_DOUBLE)


def security_summary(assets):
    print()
    print(LINE_DOUBLE)
    print(" SECURITY SUMMARY")
    print(LINE_DOUBLE)
    print_summary_counts(assets)
    count = lambda val: sum(1 for a in assets if a["security_status"] == val)
    print(f"Secure Assets       : {count('Secure')}")
    print(f"Warning Assets      : {count('Warning')}")
    print(f"Vulnerable Assets   : {count('Vulnerable')}")
    print(LINE_SINGLE)
    urgent = [a for a in assets
              if a["risk_level"] == "Critical" or a["security_status"] == "Vulnerable"]
    print("Assets needing immediate attention:")
    if not urgent:
        print("  None")
    for a in urgent:
        print(f"  - {a['asset_id']} | {a['asset_name']} | "
              f"{a['risk_level']} | {a['security_status']}")
    print(LINE_DOUBLE)


# ----------------------------------------------------------------------
# Main loop
# ----------------------------------------------------------------------
def main():
    assets = load_assets()
    actions = {
        "1": add_assets,
        "2": display_assets,
        "3": search_asset,
        "4": update_asset,
        "5": delete_asset,
        "6": security_summary,
    }
    while True:
        print_menu()
        try:
            choice = read("Enter your choice (1-7): ")
        except EOFError:
            break
        if choice == "7":
            print("Exiting... Stay secure!")
            break
        action = actions.get(choice)
        if action:
            try:
                action(assets)
            except EOFError:
                break
        else:
            error("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
