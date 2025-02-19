import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.MACRO(Press(KC.LCTL), Tap(KC.C), Release(KC.LCTL)), KC.MACRO(Press(KC.LCTL), Tap(KC.V), Release(KC.LCTL)), KC.MACRO("Hello world!"),]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
