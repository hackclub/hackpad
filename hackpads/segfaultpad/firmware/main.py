import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# Lets us use media keys!
keyboard.extensions.append(MediaKeys())

# Not sure how this is organised to KMK, this might be
# flipped x, y or perhaps both.
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D7, board.D8, board.D9, board.D10)

# Keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# Macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

# This is our desired layout:
# +-------+-------+-------+-------+
# | PREV  | PLAY  |  NEXT |  MUTE |
# +-------+-------+-------+-------+
# | UNDO  |  UP   |  REDO |VOL UP |
# +-------+-------+-------+-------+
# | LEFT  | DOWN  | RIGHT | VOL v |
# +-------+-------+-------+-------+
# | MOD   | ALT T | TILDE | SAVE  |
# +-------+-------+-------+-------+

SAVE = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.S),
    Release(KC.LCTL),
)

UNDO = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Z),
    Release(KC.LCTL),
)

# Redo: Ctrl + Y is not universal -- on some platforms it is Ctrl + Shift + Z
# FIXME
REDO = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.Y),
    Release(KC.LCTL),
)


keyboard.keymap = [
    [
        KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE,
        UNDO, KC.UP, REDO, KC.VOLU,
        KC.LEFT, KC.DOWN, KC.RIGHT, KC.VOLD,
        KC.NO, KC.LALT(KC.TAB), KC.TILDE, SAVE,
        #  ^^ No key because we don't have modifiers yet.
    ]
]

if __name__ == '__main__':
    keyboard.go()
