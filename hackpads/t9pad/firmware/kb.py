import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

kb = KMKKeyboard()

_KEY_CFG = [
board.D8, board.D9, board.D10,
board.D3, board.D6, board.D7,
board.D0, board.D1, board.D2
]

class T9Keyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(_KEY_CFG)
    # Map
    coord_mapping = [
                0, 1, 2,
                3, 4, 5,
                6, 7, 8
            ]