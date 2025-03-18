import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
row_pins = (board.GP4, board.GP2, board.GP1)

diode_orientation = DiodeOrientation.COL2ROW

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1, board.D4, board.D2, board.D1, board.D4, board.D2, board.D1]

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.Q, KC.W, KC.E, KC.R,
    KC.A, KC.S, KC.D,
    KC.Z, KC.X, KC.C]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
