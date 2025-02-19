import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306

COL1 = board.D3
COL2 = board.D6
COL3 = board.D7
COL4 = board.D11

ROW1 = board.D0
ROW2 = board.D1
ROW3 = board.D2
PUSHBUTTON = board.D8
ROTA = board.D9
ROTB = board.D10
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

keyboard = KMKKeyboard()

# Matrix configuration
keyboard.col_pins = (COL1, COL2, COL3, COL4) 
keyboard.row_pins = (ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Rotary Encoder
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

# Keymap
keyboard.keymap = [
    # 1st row: 3 keys
    [KC.DEL, KC.LCTRL(KC.TAB), KC.UP],
    # 2nd row: 4 keys
    [KC.ENTER, KC.LEFT, KC.DOWN, KC.RIGHT]
]

display = Display(
    display=driver,
    entries=[
        TextEntry(text='Yayitworks', x=0, y=0, y_anchor='M'),
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
