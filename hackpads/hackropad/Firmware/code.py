print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, SSD1306, TextEntry, ImageEntry

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

i2c_bus = busio.I2C(board.GP4, board.GP5)
display_driver = SSD1306(
    i2c=i2c_bus,
)

keyboard.col_pins = (board.GP3,board.GP4,board.GP5)
keyboard.row_pins = (board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP1, board.GP2, board.GP0, False))


DISCORD = simple_key_sequence([KC.LCMD(KC.SPACE), KC.MACRO_SLEEP_MS(1000), send_string('discord'), KC.ENTER])
SLACK = simple_key_sequence([KC.LCMD(KC.SPACE), KC.MACRO_SLEEP_MS(1000), send_string('slack'), KC.ENTER])
ARC = simple_key_sequence([KC.LCMD(KC.SPACE), KC.MACRO_SLEEP_MS(1000), send_string('ARC'), KC.ENTER])

COPY = simple_key_sequence([KC.LCMD(KC.C)])
PASTE = simple_key_sequence([KC.LCMD(KC.V)])

NEXT_DISPLAY = simple_key_sequence([KC.HYPR(KC.D)])
MAXIMISE = simple_key_sequence([KC.HYPR(KC.M)])
NEAR_MAXIMISE = simple_key_sequence([KC.HYPR(KC.N)])
BLUETOOTH = simple_key_sequence([KC.HYPR(KC.B)])

SAVE = simple_key_sequence([KC.LCMD(KC.S)])
LOCK = simple_key_sequence([KC.LCTRL(KC.LCMD(KC.Q)), KC.MACRO_SLEEP_MS(400), KC.ESCAPE])

keyboard.keymap = [
    [KC.TRANS,COPY,PASTE,
    DISCORD,SLACK,ARC,
    NEXT_DISPLAY,NEAR_MAXIMISE,MAXIMISE,
    SAVE,BLUETOOTH,LOCK]
]

encoder_handler.map = [
                        ((KC.VOLD, KC.VOLU, KC.MUTE),)
                        ]

display.entries = [
    TextEntry(text="Hackropad", x=64, y=16, x_anchor="M", y_anchor="M"), 
    TextEntry(text="By Dhyan99", x=64, y=25, x_anchor="M", y_anchor="M"), 
]

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()