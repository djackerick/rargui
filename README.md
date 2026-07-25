### First: This is only a GUI. You still need to download rar from the official sources.

# Ubuntu / Debian / Mint / Pop!_OS
sudo apt update && sudo apt install rar -y

# Fedora
sudo dnf install rar -y

# RHEL / Rocky / AlmaLinux / CentOS (requiere EPEL)
sudo dnf install epel-release -y && sudo dnf install rar -y

# Arch Linux / SteamOS / Bazzite / Manjaro / EndeavourOS
sudo pacman -S rar

# openSUSE (Leap / Tumbleweed)
sudo zypper install rar

# Binary (Universal Linux)
wget [https://www.rarlab.com/rar/rarlinux-x64.tar.gz](https://www.rarlab.com/rar/rarlinux-x64.tar.gz)
tar -xvf rarlinux-x64.tar.gz
cd rar
sudo make


### Second: You probably need to install "python3-tk"

# Ubuntu / Debian / Mint / Pop!_OS
sudo apt update && sudo apt install python3-tk -y

# Fedora / RHEL / Rocky / AlmaLinux / CentOS (requiere EPEL)
sudo dnf install python3-tkinter -y

# Arch Linux / SteamOS / Bazzite / Manjaro / EndeavourOS
sudo pacman -S tk

# openSUSE (Leap / Tumbleweed)
sudo zypper install python3-tk


### Third: You can help me to improve this GUI here:

USD-T (Tron): TLDf5X6oMTrRRvt77qbieDDWthTfpwtPim
