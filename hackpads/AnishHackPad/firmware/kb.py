
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.GP27, board.GP26)  # Define your column pins
    row_pins = (board.GP29, board.GP28)  # Define your row pins

    diode_orientation = DiodeOrientation.COL2ROW  # Set the diode orientation

    # Add additional configurations if needed
