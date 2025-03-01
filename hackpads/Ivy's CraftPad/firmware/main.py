import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("/gamemode creative"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),],
    [KC.B, KC.DELETE, KC.MACRO("/gamemode survival"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),],
    [KC.C, KC.DELETE, KC.MACRO("/time set day"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()