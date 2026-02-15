# Multi-OS Auto-Installer 🚀

A Python-based automation tool designed to detect your operating system (Windows, Debian/Ubuntu, or Arch Linux) and provide an interactive menu to install your favorite software silently.

## ✨ Features

* **OS Detection:** Automatically identifies if you are running Windows or Linux (Debian-based or Arch-based).
* **Smart Mapping:** Installs the correct package version for your OS (e.g., WinSCP on Windows vs. FileZilla on Linux).
* **AUR Support:** Automatically installs `yay` on Arch Linux if it's missing, allowing for seamless AUR package installations.
* **Silent Installation:** Uses "silent" or "headless" flags to minimize user interaction during the process.
* **Interactive Menu:** Choose specifically what you want to install or grab everything at once.

---

## 📦 Supported Software

The script currently includes pre-configured IDs for:

| Category | Applications |
| :--- | :--- |
| **Development** | Python 3.12, VSCodium, Git |
| **Design** | FreeCAD, Inkscape, OrcaSlicer |
| **Tools** | WinSCP (Windows), FileZilla (Linux), Prism Launcher, AntiMicroX |
| **Media** | VLC, LMMS, Supersonic, Steam, Firefox |

---

## 🚀 Usage

### 🪟 Windows
> **Note:** You must run the terminal as **Administrator**.

1. Ensure you have Python installed.
2. Open **PowerShell** or **Command Prompt**.
3. Navigate to the script folder.
4. Run:
   ```bash
   python installer.py

### 🐧 Linux (Arch / Debian / Ubuntu)
> **Note:** You must run the command as **Sudo**.

1. Ensure you have Python installed.
2. Open **Terminal**.
3. Navigate to the script folder.
4. Run:
   ```bash
   python installer.py
