import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.scanners.keypad import KeysScanner

PINS = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP7,
]

v1perkeeb = KMKKeyboard()
v1perkeeb.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

open_cursor = simple_key_sequence([KC.LGUI(KC.R),
                                   KC.MACRO_SLEEP_MS(100),
                                   '"C:\Users\louis\Desktop\Cursor.lnk"'
                                   ])
open_arc = simple_key_sequence([KC.LGUI(KC.R),
                                KC.MACRO_SLEEP_MS(100),
                                '"C:\Users\louis\Desktop\Arc.lnk"'
                                ])
open_spotify = simple_key_sequence([KC.LGUI(KC.R),
                                    KC.MACRO_SLEEP_MS(100),
                                    '"C:\Users\louis\Desktop\Spotify.lnk"'
                                    ])

v1perkeeb.keymap = [
    [open_cursor, open_arc, KC.LCTL(KC.C), KC.LCTL(
        KC.V), open_spotify, KC.MEDIA_PLAY_PAUSE]
]

if __name__ == '__main__':
    v1perkeeb.go()
