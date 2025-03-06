import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    keyboard.col_pins = (board.GP5, board.GP6)
    keyboard.row_pins = (board.GP7, board.GP8)

    keyboard.diode_orientation = DiodeOrientation.COL2ROW