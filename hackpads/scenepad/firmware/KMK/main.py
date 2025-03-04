from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
import microcontroller  # Use microcontroller module for RP2040 pin access

keyboard = KMKKeyboard()

# Define the pins each key is connected to
keyboard.row_pins = (microcontroller.pin.GP0, microcontroller.pin.GP1, microcontroller.pin.GP2, microcontroller.pin.GP3)  # RP2040-compatible pin references
keyboard.diode_orientation = None  # No diode/matrix needed

# Define the keymap
keyboard.keymap = [
    [KC.LCTRL(KC.P), KC.LCTRL(KC.N), KC.LSFT(KC.H), KC.LSFT(KC.O)]  # Maps keys to correct shortcuts
]

if __name__ == '__main__':
    keyboard.go()
