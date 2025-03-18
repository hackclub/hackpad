import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()


COL1 = board.GP0
COL2 = board.GP1
COL3 = board.GP2
COL4 = board.GP3

ROW1 = board.GP4
ROW2 = board.GP5

# Rotary encoder pins
ROTA = board.GP6
ROTB = board.GP7
PUSHBUTTON = board.GP8

# Matrix settings: define rows, columns, and diode orientation
keyboard.col_pins = (COL1, COL2, COL3, COL4)  # 4 columns
keyboard.row_pins = (ROW1, ROW2)  # 2 rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)


keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.X), KC.LALT(KC.SPACE)],  # Row 1
    [KC.LCTRL(KC.S), KC.LCTRL(KC.A), KC.LCTRL(KC.Z), KC.LCTRL(KC.P)],  # Row 2
]
if __name__ == '__main__':
    keyboard.go()
