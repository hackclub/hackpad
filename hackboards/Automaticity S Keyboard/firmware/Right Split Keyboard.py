from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digital import DiodeOrientation
import board

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4, board.D3, board.D2, board.D1, board.D0) 
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D8, board.D9, board.D10,board.D11,board.D12) 
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.SPACE, KC.N, KC.H, KC.Y ,KC.N6],
    [KC.RALT, KC.M, KC.J, KC.U, KC.N7],
    [KC.PSCREEN, KC.COMMA, KC.K, KC.I, KC.N8],
    [KC.RCTRL, KC.DOT, KC.L, KC.O, KC.N9],
    [KC.RGUI, KC.SLASH, KC.SCOLON, KC.P, KC.N0],
    [KC.LEFT, KC.SHIFT, KC.QUOTE, KC.LBRACKET, KC.MINUS],
    [KC.DOWN, KC.UP, KC.F1, KC.RBRACKET, KC.EQUAL],
    [KC.RIGHT, KC.F2, KC.ENTER, KC.BSLASH, KC.BSPACE],

]

if __name__ == '__main__':
    keyboard.go()
