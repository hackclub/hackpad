# You import all the IOs of your board
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP29, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3],
    [KC.N4, KC.N5, KC.N6],
    [KC.N7, KC.N8, KC.N9]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()