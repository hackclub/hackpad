import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Changed keymap to have CTRL and X, C, V keys
keyboard.keymap = [
    [KC.LCTL, KC.X, KC.C, KC.V]
]

if __name__ == '__main__':
    keyboard.go()
