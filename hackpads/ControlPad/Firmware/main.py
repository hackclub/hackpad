
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display.ssd1306 import SSD1306
import busio

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.append(encoder_handler)

keyboard.col_pins = (board.GP10, board.GP9, board.GP8)
keyboard.row_pins = (board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [ 
    [KC.F1, KC.F2, KC.F3, 
    KC.F4, KC.F5, KC.F6,
    KC.F7, KC.F8, KC. F9,
    KC.F10, KC.F11, KC.F12 
    ]
]

encoder_handler = EncoderHandler()
keyboard.append(encoder_handler)
encoder_handler.pins = ((board.GP6, board.GP7, board.GP8),)  

encoder_handler.map = [(
    (KC.VOLU, KC.VOLD)
    
)]

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver=SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Control Pad', x=0, y=0, y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()