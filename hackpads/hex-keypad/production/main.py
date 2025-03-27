# You import all the IOs of your board import board
# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
col_pins = (board.MOSI, board.MISO, board.SCK, board.RX)
row_pins = (board.D28, board.D29, board.SDA, board.SCL)

keyboard.keymap = [[KC.P1, KC.P2, KC.P3, KC.LSFT(KC.A)],
                   [KC.P4, KC.P5, PC.P6, KC.LSFT(KC.B)],
                   [KC.P7, KC.P8, KC.P9, KC.LSFT(KC.C)],
                   [KC.P0, KC.LSFT(KC.E), KC.LSFT(KC.F), KC.LSFT(KC.D)]]

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
# keyboard.keymap = [
#    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
# ]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
