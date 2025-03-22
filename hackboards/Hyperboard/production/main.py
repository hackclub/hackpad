import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Define your pins here!
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.row_pins = (board.GP16, board.GP21, board.GP22, board.GP23, board.GP24, board.GP25, board.GP26)
diode_orientation = DiodeOrientation.COL2ROW

#TODO Hyper/Layer3 and Fn key
#TODO Add the other layers
keyboard.keymap = [
    [ #Layer1
    KC.HyperSlashLayer3!!, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL,
    KC.GRAVE, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUAL, KC.BACKSPACE,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.ENTER,
    KC.ESC, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE, KC.BACKSLASH,
    KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.PERIOD, KC.SLASH, KC.RSHIFT, KC.UP, KC.PRTSC,
    KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.SPACE, KC.RALT, KC.FnKey!!, KC.LEFT, KC.DOWN, KC.RIGHT,
    ],
    [ #Layer2 (shift or Fn) (Capital letters and Symbols and Media keys on F_keys)

    ],
    [ #Layer3 (hyper?) ()

    ]
]


# Start kmk!
if __name__ == '__main__':
    keyboard.go()


    