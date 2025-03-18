import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    COL_0 = board.D3
    COL_1 = board.D2
    COL_2 = board.D1

    ROW_0 = board.D7
    ROW_1 = board.D6
    ROW_2 = board.D5

    ROT_A = board.D9
    ROT_B = board.D8
    ROT_S1 = board.D10
    
    keyboard.col_pins = (COL_0, COL_1, COL_2, ROT_S1)
    keyboard.row_pins = (ROW_0, ROW_1, ROW_2)
    keyboard.diode_orientation = DiodeOrientation.COL2ROW