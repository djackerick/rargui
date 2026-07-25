[Leer en Español](README.es.md)

# RarGUI
A simple Python (Tkinter) GUI for compressing RAR files under Linux.

<img width="599" height="469" alt="Image" src="https://github.com/user-attachments/assets/b09b0548-cae5-481a-bca9-53d026a2c18c" />

## First: This is only a GUI. You still need to download rar from the official sources.

Ubuntu / Debian / Mint / Pop!_OS
```bash
sudo apt update && sudo apt install rar -y
```

Fedora
```bash
sudo dnf install rar -y
```

RHEL / Rocky / AlmaLinux / CentOS (requiere EPEL)
```bash
sudo dnf install epel-release -y && sudo dnf install rar -y
```

Arch Linux / SteamOS / Bazzite / Manjaro / EndeavourOS
```bash
sudo pacman -S rar
```

openSUSE (Leap / Tumbleweed)
```bash
sudo zypper install rar
```

Binary (Universal Linux)
```bash
wget [https://www.rarlab.com/rar/rarlinux-x64.tar.gz](https://www.rarlab.com/rar/rarlinux-x64.tar.gz)
tar -xvf rarlinux-x64.tar.gz
cd rar
sudo make
```


## Second: You probably need to install "python3-tk"

Ubuntu / Debian / Mint / Pop!_OS
```bash
sudo apt update && sudo apt install python3-tk -y
```

Fedora / RHEL / Rocky / AlmaLinux / CentOS (requiere EPEL)
```bash
sudo dnf install python3-tkinter -y
```

Arch Linux / SteamOS / Bazzite / Manjaro / EndeavourOS
```bash
sudo pacman -S tk
```

openSUSE (Leap / Tumbleweed)
```bash
sudo zypper install python3-tk
```


## Third: Give execution (+x) permissions
This is valid for every distro
```bash
chmod +x rargui.py
```


## Fourth: You can help me by just donating here:

USD-T (Tron):
```bash
TLDf5X6oMTrRRvt77qbieDDWthTfpwtPim
```
