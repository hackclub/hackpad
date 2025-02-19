import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keyboard import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
# from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D4, board.D3]

keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()
