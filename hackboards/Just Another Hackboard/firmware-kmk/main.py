print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules import RGB
from kmk.keys import KC
from kmk.handlers.stock import led_toggle
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()
keyboard.matrix = MatrixScanner(columns=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,],
                                rows=[board.GP15, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26]
                                )

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.ESCAPE, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCREEN, KC.NO],
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUALS, KC.BACKSPACE, KC.DELETE],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.ENTER, KC.HOME],
    [KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.HASH, KC.END, KC.NO],
    [KC.LSHIFT, KC.BSLASH, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.NO],
    [KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.ALT, KC.RGUI, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO]
]

enHandler = EncoderHandler()
keyboard.modules.append(enHandler)
enHandler.pins = ((board.GP17, board.GP16, board.GP18),)
enHandler.map = [(KC.VOLU, KC.VOLD, KC.MUTE)]

rgb = RGB(pixel_pin=board.GP27, num_pixels=82)
rgb.brightness = 100
rgb.enabled = True
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()