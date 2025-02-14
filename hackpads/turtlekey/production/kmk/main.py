from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
import board

keyboard = KMKKeyboard()

COL_0 = board.D3
COL_1 = board.D2
COL_2 = board.D1

ROW_0 = board.D7
ROW_1 = board.D6
ROW_2 = board.D5

ROT_A = board.D9
ROT_B = board.D8
ROT_S1 = board.D10

keyboard.col_pins = (COL_0, COL_1, COL_2, ROT_S1)
keyboard.row_pins = (ROW_0, ROW_1, ROW_2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


enc_handler = EncoderHandler()
keyboard.modules.append(enc_handler)
enc_handler.pins = ((ROT_A, ROT_B, None))
enc_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

keyboard.keymap = [
    [KC.T,      KC.U,   KC.R, KC.AUDIO_VOL_DOWN,KC.AUDIO_VOL_UP],
    [KC.T,      KC.L,     KC.E],
    [KC.E,      KC.E,     KC.E],
]


if __name__ == '__main__':
    keyboard.go()