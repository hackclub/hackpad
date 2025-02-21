# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
keyboard.pins_col = [board.GPIO2, board.GPIO4, board.GPIO03]
keyboard.pins_row = [board.GPIO6, board.GPIO7, board.GPIO0]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    keyboard=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    KC.1,
    KC.2,
    KC.3,
    KC.4,
    KC.5,
    KC.6,
    KC.7,
    KC.8,
    KC.SPACE,
    KC.0,
    MEDIA.MUTE
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
