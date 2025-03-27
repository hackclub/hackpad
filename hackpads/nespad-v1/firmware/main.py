# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC


# This is the main instance of your keyboard
nespad = KMKKeyboard()

# Add the macro extension
macros = Macros()
nespad.modules.append(macros)

# Define your pins here!
PINS = [board.D6, board.D7, board.D26, board.D27, board.D28, board.D29]

# Tell kmk we are not using a key matrix
nespad.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

#Temporarily set to a typical nes controller keys, up/down/left/right and a/b, no start/select though.

nespad.keymap = [
    [KC.A, KC.B, KC.UP, KC.DOWN, KC.LEFT, KC.RIGHT]
]

# Start kmk!
if __name__ == '__main__':
    nespad.go()