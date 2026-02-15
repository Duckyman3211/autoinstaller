import platform
import subprocess
import os
import sys

# Mapping of software to their respective package manager IDs
# If a key (e.g., 'winget') is missing, the app will be skipped on that OS.
SOFTWARE = {
    "FreeCAD": {"winget": "FreeCAD.FreeCAD", "pacman": "freecad", "apt": "freecad"},
    "Firefox": {"winget": "Mozilla.Firefox", "pacman": "firefox", "apt": "firefox"},
    "VSCodium": {"winget": "VSCodium.VSCodium", "yay": "vscodium-bin", "apt": "vscodium"},
    "Python 3.12": {"winget": "Python.Python.3.12", "pacman": "python", "apt": "python3.12"},
    "Inkscape": {"winget": "Inkscape.Inkscape", "pacman": "inkscape", "apt": "inkscape"},
    "WinSCP": {"winget": "WinSCP.WinSCP"},  # Windows Only
    "FileZilla": {"pacman": "filezilla", "apt": "filezilla"},  # Linux Only
    "AntiMicroX": {"winget": "AntiMicroX.AntiMicroX", "pacman": "antimicrox", "apt": "antimicrox"},
    "Steam": {"winget": "Valve.Steam", "pacman": "steam", "apt": "steam"},
    "LMMS": {"winget": "LMMS.LMMS", "pacman": "lmms", "apt": "lmms"},
    "VLC": {"winget": "VideoLAN.VLC", "pacman": "vlc", "apt": "vlc"},
    "OrcaSlicer": {"winget": "SoftFever.OrcaSlicer", "yay": "orcaslicer-bin", "apt": "orcaslicer"},
    "Prism Launcher": {"winget": "PrismLauncher.PrismLauncher", "pacman": "prismlauncher", "apt": "prismlauncher"},
    "Supersonic": {"winget": "Sudo-Standard.Supersonic", "yay": "supersonic-bin", "apt": "supersonic"},
}

def run_command(command):
    """Executes a shell command and returns True if successful."""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def ensure_yay():
    """Checks for Yay on Arch Linux, installs it if missing."""
    if os.path.exists("/usr/bin/yay"):
        return True
    
    print("\n[!] Yay (AUR helper) not found. Installing now...")
    commands = [
        "sudo pacman -S --needed --noconfirm base-devel git",
        "git clone https://aur.archlinux.org/yay.git /tmp/yay_build",
        "cd /tmp/yay_build && makepkg -si --noconfirm",
        "rm -rf /tmp/yay_build"
    ]
    for cmd in commands:
        if not run_command(cmd):
            print(f"Failed to execute: {cmd}")
            return False
    return True

def get_package_manager():
    """Detects the OS and returns the appropriate manager key."""
    sys_type = platform.system().lower()
    
    if sys_type == "windows":
        return "winget"
    
    if sys_type == "linux":
        if os.path.exists("/usr/bin/pacman"):
            ensure_yay()
            return "arch" # Custom key to handle both pacman and yay
        if os.path.exists("/usr/bin/apt"):
            return "apt"
            
    return None

def install_app(app_name, manager):
    """Executes the installation command based on the manager."""
    data = SOFTWARE[app_name]
    cmd = ""

    if manager == "arch":
        if "yay" in data:
            cmd = f"yay -S --noconfirm {data['yay']}"
        elif "pacman" in data:
            cmd = f"sudo pacman -S --noconfirm {data['pacman']}"
    
    elif manager == "winget":
        if "winget" in data:
            cmd = f"winget install --id {data['winget']} --silent --accept-source-agreements --accept-package-agreements"
            
    elif manager == "apt":
        if "apt" in data:
            cmd = f"sudo apt update && sudo apt install -y {data['apt']}"

    if cmd:
        print(f"\n>>> Installing {app_name}...")
        run_command(cmd)
    else:
        print(f"\n[?] Skipping {app_name}: Not supported for this OS.")

def main():
    manager = get_package_manager()
    if not manager:
        print("Error: Unsupported Operating System or Package Manager.")
        sys.exit(1)

    print("========================================")
    print(f" Detected System Manager: {manager.upper()} ")
    print("========================================\n")

    # Filter apps available for the current OS
    available_apps = [name for name, os_data in SOFTWARE.items() 
                      if (manager == "arch" and ("pacman" in os_data or "yay" in os_data)) 
                      or (manager in os_data)]

    for i, app in enumerate(available_apps, 1):
        print(f"{i}. {app}")

    print("\nOptions:")
    print("- Enter numbers separated by commas (e.g., 1,3,5)")
    print("- Type 'all' to install everything")
    print("- Type 'exit' to quit")
    
    choice = input("\nYour choice: ").strip().lower()

    if choice == 'exit':
        sys.exit(0)
    
    to_install = []
    if choice == 'all':
        to_install = available_apps
    else:
        try:
            indices = [int(x.strip()) - 1 for x in choice.split(",")]
            to_install = [available_apps[i] for i in indices]
        except (ValueError, IndexError):
            print("Invalid input. Please restart the script.")
            sys.exit(1)

    for app in to_install:
        install_app(app, manager)

    print("\nDone! All selected applications have been processed.")

if __name__ == "__main__":
    main()