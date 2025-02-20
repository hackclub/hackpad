import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D7, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# I dont want to do macros quite yet because they're pretty complicated
keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

if __name__ == '__main__':
    keyboard.go()