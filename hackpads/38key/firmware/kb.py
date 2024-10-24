import board;

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    keyboard.col_pins = (board.GP1, board.GP0, board.GP28, board.GP29, board.GP3)
    keyboard.row_pins = (board.GP26, board.GP27, board.GP4, board.GP5)

    keyboard.diode_orientation = DiodeOrientation.COL2ROW