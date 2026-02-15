Multi-OS Auto-Installer 🚀

A Python-based automation tool designed to detect your operating system (Windows, Debian/Ubuntu, or Arch Linux) and provide an interactive menu to install your favorite software silently.
Features

*    OS Detection: Automatically identifies if you are running Windows or Linux (Debian-based or Arch-based).

*    Smart Mapping: Installs the correct package version for your OS (e.g., WinSCP on Windows vs. FileZilla on Linux).

*    AUR Support: Automatically installs yay on Arch Linux if it's missing, allowing for seamless AUR package installations.

*    Silent Installation: Uses "silent" or "headless" flags to minimize user interaction during the process.

*    Interactive Menu: Choose specifically what you want to install or grab everything at once.

Supported Software

The script currently includes pre-configured IDs for:

*    Development: Python 3.12, VSCodium, Git

*    Design: FreeCAD, Inkscape, OrcaSlicer

*    Tools: WinSCP (Win), FileZilla (Linux), Prism Launcher, AntiMicroX

*    Media: VLC, LMMS, Supersonic, Steam, Firefox

Usage
Windows

    Open PowerShell or Command Prompt as Administrator.

    Navigate to the script folder.

    Run:

    `python setup.py`

Linux (Arch / Debian / Ubuntu)

    Open your terminal.

    Ensure you have Python installed.

    Run:

    `python3 setup.py`

    Note: The script will prompt for sudo password to perform installations.

How it Works

The script uses platform and os modules to check for system binaries.

*    On Windows, it leverages Winget, the native Windows Package Manager.

*    On Debian/Ubuntu, it uses APT.

*    On Arch, it uses Pacman for official repos and Yay for the Arch User Repository (AUR).