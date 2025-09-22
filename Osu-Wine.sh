#!/bin/bash

# Create ~/bin if it doesn't exist
mkdir -p "$HOME/bin"

# Write the optimized osu launcher script
cat << 'EOF' > "$HOME/bin/osu"
#!/bin/bash

# -----------------------------
# ENVIRONMENT OPTIMIZATIONS
# -----------------------------
# NVIDIA offload
export __NV_PRIME_RENDER_OFFLOAD=1
export __GLX_VENDOR_LIBRARY_NAME=nvidia
export __VK_LAYER_NV_optimus=NVIDIA_only
export __NV_PRIME_RENDER_OFFLOAD_PROVIDER=NVIDIA-G0

# OpenGL / GPU
export __GL_THREADED_OPTIMIZATIONS=1  # Multi-threaded OpenGL
export __GL_SYNC_TO_VBLANK=0          # Disable vsync
export __GL_YIELD="USLEEP"            # Reduce CPU busy-waiting

# Wine / DXVK
export WINEFSYNC=1
export WINEESYNC=1
export DXVK_ASYNC=1
export WINE_DISABLE_WRITE_WATCH=1

# -----------------------------
# OPTIONAL NVIDIA POWER SETTINGS
# -----------------------------
# Uncomment if you want to force max GPU clocks
# sudo nvidia-smi -i 0 -pm 1 >/dev/null 2>&1
# sudo nvidia-smi -i 0 -pl 120 >/dev/null 2>&1

# -----------------------------
# LAUNCH osu! IN BACKGROUND
# -----------------------------
# High CPU priority
renice -n -5 $$ >/dev/null 2>&1

# Launch osu silently with GameMode and NVIDIA GPU
nohup prime-run gamemoderun osu-wine >/dev/null 2>&1 & disown
EOF

# Make it executable
chmod +x "$HOME/bin/osu"

# Add ~/bin to PATH if not already
if ! echo "$PATH" | grep -q "$HOME/bin"; then
    SHELL_RC="$HOME/.bashrc"
    [ -n "$ZSH_VERSION" ] && SHELL_RC="$HOME/.zshrc"
    echo 'export PATH="$HOME/bin:$PATH"' >> "$SHELL_RC"
    echo "[+] Added ~/bin to PATH in $SHELL_RC"
    echo "⚠️  Restart your terminal or run: source $SHELL_RC"
fi

echo "[✓] osu launcher created at ~/bin/osu"
