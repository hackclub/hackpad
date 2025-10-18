import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC, key
from kmk.modules.macros import Macros, UnicodeModeIBus, UnicodeModeMacOS, UnicodeModeWinC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
row_pins = (board.GP3, board.GP4, board.GP2)

diode_orientation = DiodeOrientation.COL2ROW

macros = Macros(unicode_mode=UnicodeModeMacOS)
keyboard.modules.append(macros)

def switch_um(keyboard):
    if macros.unicode_mode == UnicodeModeIBus:
        macros.unicode_mode = UnicodeModeMacOS
    elif macros.unicode_mode == UnicodeModeMacOS:
        macros.unicode_mode = UnicodeModeWinC
    else:
        macros.Unicode_mode = UnicodeModeIBus

UCCYCLE = Key(code=None, on_press=switch_um)

keyboard.keymap = [
    [KC.MACRO("Hello World!"), KC.MACRO("¯\_(ツ)_/¯"), KC.MACRO("◉︵◉"), KC.MACRO("\(^o^)/"),
    KC.MACRO("😁"), KC.F, KC.L, KC.W,
    KC.MACRO("❤️"), KC.MACRO("👍"), KC.A, KC.B]
]

if __name__ == '__main__':
    keyboard.go()