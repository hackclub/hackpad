'''
Aether Pad
'''
import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306

# Pinout
COL1 = board.D10
COL2 = board.D9
COL3 = board.D8
COL4 = board.D7
ROW1 = board.D3
ROW2 = board.D2
PUSHBUTTON = board.D6
ROTA = board.D0
ROTB = board.D1
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

keyboard = KMKKeyboard()

#matrix settings
keyboard.col_pins = (COL1, COL2, COL3, COL4)
keyboard.row_pins = (ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

#Screen
display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Aether Pad', x=0, y=0, y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)
keyboard.extensions.append(display)

# Keymap
keyboard.keymap = [
    [KC.LCTRL(KC.LSHIFT(KC.TAB)), KC.LCTRL(KC.M), KC.LCTRL(KC.TAB), KC.LCTRL(KC.C),
     KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.LCTRL(KC.V)
    ]
]

if __name__ == '__main__':
    keyboard.go()
