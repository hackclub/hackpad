
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.GP3, board.GP2, board.GP1, board.GP0, board.GP7, board.GP6, board.GP29]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G,]
]

if __name__ == '__main__':
    keyboard.go()
