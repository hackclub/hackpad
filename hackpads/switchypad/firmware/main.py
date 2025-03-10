# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeyMatrix
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
ROW_PINS = [board.D3, board.D4, board.D2]
COL_PINS = [board.D1, board.D0, board.D5]

# Tell kmk we are using a key matrix
keyboard.matrix = KeyMatrix(
    rows=ROW_PINS,
    cols=COL_PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.B, KC.C],
    [KC.D, KC.E, KC.F],
    [KC.G, KC.H, KC.I]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()