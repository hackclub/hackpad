# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3, board.GP4, board.GP5)
keyboard.row_pins = (board.GP0, board.GP1, board,GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
	    [KC.N1, KC.N2, KC.N3,
	    KC.N4, KC.N5, KC.N6,
	    KC.N7, KC.N8, KC.N9]
]
if __name__ == '__main__':
    keyboard.go()