import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.D2, board.D3, board.D4, board.D5)
    row_pins = (board.D1, board.D7)
    diode_orientation = DiodeOrientation.ROW2COL