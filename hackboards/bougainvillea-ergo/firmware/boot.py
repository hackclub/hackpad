import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

# Disable console and MIDI to save memory
usb_cdc.disable()

# Uncomment the following line if you want to disable the USB drive
# storage.disable_usb_drive()

# Uncomment these lines to use a button connected to GP22 to disable USB drive
# For safety - if button is pressed during boot, USB drive will be enabled
# This allows recovery if your keyboard code has errors
"""
button = digitalio.DigitalInOut(board.GP22)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive()
"""

print("Starting keyboard...") 