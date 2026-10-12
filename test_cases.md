# Test Cases – Cybersecurity Asset Inventory System

All test cases were executed by running `src/asset_inventory.py` with scripted input and checking the output.

| ID | Feature | Test Input | Expected Result | Result |
|----|---------|-----------|-----------------|--------|
| TC01 | Add asset | Add 3 valid assets (A101, A102, A103) | Each asset saved; `Asset A10x added successfully.` shown | Pass |
| TC02 | Display assets | Menu option 2 | All assets listed with totals (Total Assets: 3) | Pass |
| TC03 | Search by name | Search `web` | 1 asset found (Web-Server) | Pass |
| TC04 | Update asset | Update A102 → Operating System = `Ubuntu 22.04` | `Operating System updated successfully.` and new value shown | Pass |
| TC05 | Delete asset | Delete A104, confirm `yes` | `Asset A104 deleted successfully.` | Pass |
| TC06 | Security summary | Menu option 6 | Critical = 1, Vulnerable = 1, A102 listed under immediate attention | Pass |
| TC07 | Duplicate ID | Add asset with ID `A101` again | `Asset ID A101 already exists.` – asks again | Pass |
| TC08 | Invalid asset type | Type = `Laptop` | Error listing valid types – asks again | Pass |
| TC09 | Invalid IP | IP = `999.1.1.1` | `Invalid IP address.` – asks again | Pass |
| TC10 | Invalid risk level | Risk = `Severe` | Error listing Low/Medium/High/Critical – asks again | Pass |
| TC11 | Invalid security status | Status = `Unknown` | Error listing Secure/Warning/Vulnerable – asks again | Pass |
| TC12 | Invalid menu choice | Choice = `9` | `Invalid choice. Please enter a number from 1 to 7.` | Pass |
| TC13 | Invalid asset count | Number of assets = `abc` | `Please enter a whole number greater than 0.` | Pass |
| TC14 | Empty inventory | Display with no assets | `No assets found.` | Pass |
| TC15 | Search – no match | Search `zzz` | `No matching asset found.` | Pass |
| TC16 | Update/Delete unknown ID | ID = `A999` | `Asset not found.` | Pass |
| TC17 | Cancel delete | Delete A101, answer `no` | `Delete cancelled.`; asset still exists | Pass |
| TC18 | Invalid IP on update | New IP = `300.1.1.1`, then `192.168.1.11` | Error, then value accepted | Pass |
| TC19 | Search by type | Search `router` | Core-Router returned | Pass |
| TC20 | Data persistence | Close program, run again, display | Previously added assets are still present | Pass |
