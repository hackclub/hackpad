from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digital import DiodeOrientation
import board

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2) 
keyboard.row_pins = (board.D3, board.D4, board.D5) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define keymap
keyboard.keymap = [
    [KC.Q, KC.W, KC.E],
    [KC.A, KC.S, KC.D],
    [KC.Z, KC.X, KC.C]
]

if __name__ == '__main__':
    keyboard.go()
