import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

oled = Oled(
    OledData(
        corner_one={OledReactionType.STATIC: ["Layer"]},
        corner_two={OledReactionType.LAYER: ["1", "2", "3"]},
        corner_three={OledReactionType.STATIC: ["KMK"]},
        corner_four={OledReactionType.STATIC: ["OuiCaptures"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)

keyboard.extensions.append(oled)

PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)), KC.NO, KC.NO]
]
if __name__ == '__main__':
    keyboard.go()


