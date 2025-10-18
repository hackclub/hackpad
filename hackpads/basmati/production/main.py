import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.DELETE, 
        KC.MACRO(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)), 
        KC.MACRO(Press(KC.LCMD), Tap(KC.V), Release(KC.LCMD)), 
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD))
    ]
]

if __name__ == '__main__':
    keyboard.go()