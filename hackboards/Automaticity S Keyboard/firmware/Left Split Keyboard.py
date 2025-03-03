from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digital import DiodeOrientation
import board

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4, board.D3, board.D2, board.D1, board.D0) 
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D8, board.D9, board.D10) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.SPACE, KC.B, KC.G, KC.T ,KC.N5],
    [KC.LALT, KC.V, KC.F, KC.R, KC.N4],
    [KC.LGUI, KC.C, KC.D, KC.E, KC.N3],
    [KC.LCTRL, KC.X, KC.S, KC.W, KC.N2],
    [KC.TRNS, KC.Z, KC.A, KC.Q, KC.N1],
    [KC.GRAVE, KC.SHIFT, KC.CAPSLOCK, KC.TAB, KC.ESCAPE],
]

if __name__ == '__main__':
    keyboard.go()