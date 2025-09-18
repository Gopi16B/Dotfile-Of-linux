#!/bin/bash

# Update system
sudo pacman -Syu --noconfirm

# Install yay if not installed
if ! command -v yay &> /dev/null
then
    sudo pacman -S --needed --noconfirm base-devel git
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si --noconfirm
    cd ..
    rm -rf yay
fi

# Packages to install via yay (AUR + official repos)
YAY_PACKAGES=(
  gamemode
  micro
  kitty
  chmod
  nvidia-hook
  nvidia-inst
  nvidia-prime
  preload
  steam
  sklauncher-bin
  spotify
  tk
  viber
  visual-studio-code-bin
  wine
  wine-gecko
  wine-mono
  winetricks
)

echo "Installing yay packages..."
for pkg in "${YAY_PACKAGES[@]}"; do
    yay -S --needed --noconfirm "$pkg"
done

# Only one Flatpak app
FLATPAK_APP="org.vinegarhq.Sober"

echo "Installing Flatpak app: $FLATPAK_APP"
flatpak install -y flathub "$FLATPAK_APP"

echo "All selected apps installed!"
