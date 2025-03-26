# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import KeysScanner, DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.extensions.append(KeysScanner())

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.NO, KC.NO],
    [KC.GRAVE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUAL, KC.BACKSPACE, KC.NO, KC.NO, KC.NO],
    [KC.TAB,KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LEFT_BRACE, KC.RIGHT_BRACE, KC.BSLS, KC.NO, KC.NO, KC.NO],
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE, KC.ENTER],
    [KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.ARROW_UP,],
    [KC.LCTRL, KC.LGUI, KC.LEFT_ALT, KC.SPACE, KC.RIGHT_ALT, KC.RGUI, KC.RCTRL, KC.ARROW_LEFT, KC.ARROW_DOWN, KC.ARROW_RIGHT],
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()