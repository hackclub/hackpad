# MCU Settings
MCU = rp2040

# Bootloader Selection (usually rp2040)
BOOTLOADER = rp2040

# Build options
# You can enable or disable features here
RGBLIGHT_ENABLE = yes       # Disable RGB lighting by default
RGBLIGHT_DRIVER = ws2812
MOUSEKEY_ENABLE = no       # Disable mouse keys
EXTRAKEY_ENABLE = yes      # Enable extra keys (media control, etc.)
CONSOLE_ENABLE = no        # Disable console output
COMMAND_ENABLE = no        # Disable command feature

# Define matrix size (rows x columns)
MATRIX_ROWS = 4
MATRIX_COLS = 4

# Enable USB Features
VUSB_ENABLE = no           # Disable virtual USB for this project
USB_VID = 0x03A8           # Vendor ID
USB_PID = 0xA701           # Product ID for the macropad

# Set processor frequency
F_CPU = 12000000

# Enable bootmagic lite for keymap reset
BOOTMAGIC_ENABLE = lite    # Allows for holding a key during boot to reset QMK

# Enable encoder support if needed
ENCODER_ENABLE = yes        # Disable by default
