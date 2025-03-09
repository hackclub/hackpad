import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner

class MacroPad(KMKKeyboard):
    def __init__(self):
        # Key matrix pins
        self.direct_pins = [
            board.D5,
            board.D6,
            board.D7,
            board.D8,
        ]

        self.led1 = board.D9
        self.led2 = board.D10

        self.scanner = KeysScanner(
            pins=self.direct_pins,
            value_when_pressed=False,
            pull=True,
        )