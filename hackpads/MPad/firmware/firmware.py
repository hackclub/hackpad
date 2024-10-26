print("Starting")
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
import board

keyboard = KMKKeyboard()

#pins
COL_0 = board.D0
COL_1 = board.D1
COL_2 = board.D2
COL_3 = board.D3
ROW_0 = board.D4
ROW_1 = board.D5
ROW_2 = board.D6
ROW_3 = board.D7
ROT_A = board.D9
ROT_B = board.D10
ROT_S2 = board.D8

# matrix-configuration
keyboard.col_pins = (COL_0, COL_1, COL_2, COL_3, ROT_S2)
keyboard.row_pins = (ROW_0, ROW_1, ROW_2, ROW_3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

# Rotary Encoder
enc_handler = EncoderHandler()
keyboard.modules.append(enc_handler)
enc_handler.pins = ((ROT_A, ROT_B, None))
enc_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.C),KC.LCTRL(KC.V),KC.LCTRL(KC.X),KC.LCTRL(KC.S),KC.MUTE,
     KC.MEDIA_PREV_TRACK,KC.MEDIA_PLAY_PAUSE,KC.MEDIA_NEXT_TRACK,KC.LALT(KC.LCTRL(KC.TAB)),
     KC.LCTRL(KC.LSHIFT(KC.R)),KC.LCTRL(KC.LSHIFT(KC.TAB)),KC.LGUI(KC.TAB),KC.LALT(KC.F4),
     KC.LGUI(KC.LCTRL(KC.D)),KC.LGUI(KC.LCTRL(KC.LEFT)),KC.LGUI(KC.LCTRL(KC.RIGHT)),KC.LGUI(KC.LCTRL(KC.F4))
     ]
    ]


if __name__ == '__main__':
    keyboard.go()