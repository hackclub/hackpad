# <boot.py>
# Include this file at the root of the CIRCUITPY drive if
# you want to disable the USB drive and serial interface
# unless you press and hold key 10 while booting
import board
import digitalio
import storage
import usb_cdc

# Need this to make the keyboard visible in the BIOS
# This is a macropad so unlikely that we'll need it
# import usb_hid
# usb_hid.enable(boot_device=1)

# The USB drive (CIRCUITPY), and serial interface (REPL)
# are enabled by default
#
# If the key on pin D10 is not held during boot,
# execute the code to disable the USB drive and serial interface.
# (Hold the key to mount the drive and serial interface)
#
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial

bypass_key = digitalio.DigitalInOut(board.D10)
bypass_key.pull = digitalio.Pull.UP

if bypass_key.value:
    # Disable the CIRCUITPY USB drive
    storage.disable_usb_drive()

    # Disable both serial devices
    # Equivalent to usb_cdc.enable(console=False, data=False)
    usb_cdc.disable()

bypass_key.deinit()