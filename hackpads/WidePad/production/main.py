import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]
col_pins = [board.P3, board.D3, board.D4, board.D2, board.D1]
col_pins = [board.P4, board.P2, board.P1]

keyboard.matrix = KeysScanner(
    column_pins=col_pins,
    row_pins=row_pins,
)

keyboard.keymap = [
    [KC.MACRO("Hello World!")]
]

if __name__ == '__main__':
    keyboard.go()
