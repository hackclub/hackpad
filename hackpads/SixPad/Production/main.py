import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.macros import Macros
from kmk.scanners.keypad import MatrixScanner

# Initialize keyboard
keyboard = KMKKeyboard()

# Add Macros module (optional, for advanced macros)
macros = Macros()
keyboard.modules.append(macros)

# Define row and column pins from the schematic
ROW_PINS = [board.D26, board.D27, board.D2]  # ROW_0, ROW_1, ROW_2
COL_PINS = [board.D29, board.D6]  # COL_0, COL_1

# Configure the key matrix
keyboard.matrix = MatrixScanner(
    rows=ROW_PINS,
    cols=COL_PINS,
    value_when_pressed=False,  # Adjust if necessary
)

# Define keymap (update with preferred key functions)
keyboard.keymap = [
    [KC.A, KC.B],  # ROW_0
    [KC.C, KC.D],  # ROW_1
    [KC.E, KC.F],  # ROW_2
]

# Start KMK
if __name__ == '__main__':
    keyboard.go()
