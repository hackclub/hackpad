# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
#PINS = [board.D3, board.D4, board.D2, board.D1]
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10)

# Tell kmk we are not using a key matrix
#keyboard.matrix = KeysScanner(
#    pins=PINS,
#    value_when_pressed=False,
#)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.NLCK, KC.P7, KC.P8, KC.P9, KC.MEDIA_PREV_TRACK, 
    KC.P4, KC.P5, KC.P6, KC.MEDIA_PLAY_PAUSE,
    KC.P1, KC.P2, KC.P3, KC.MEDIA_NEXT_TRACK,
    KC.P0, KC.PDOT, KC.PENT] # Media keys prev/next are windows-specific
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()