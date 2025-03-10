# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
keyboard.col_pins = (board.A0, board.A1, board.A2)
keyboard.row_pins = (board.A3, board.MISO, board.MOSI)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [[KC.RABK, KC.DOT, KC.COMMA], [KC.LABK, KC.PLUS, KC.LBRACKET], [KC.MINUS, KC.NO, KC.RBRACKET]]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()