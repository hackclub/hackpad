import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306

COL1 = board.D2
COL2 = board.D3
COL3 = board.D4
ROW1 = board.D5
ROW2 = board.D6
ROW3 = board.D7
PUSHBUTTON = board.D8
ROTA = board.D9
ROTB = board.D10
i2c_bus = busio.I2C(board.D4, board.D5)

display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

keyboard = KMKKeyboard()

keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = None

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

display = Display(
    display=display_driver,
    entries=[TextEntry(text='AARYAV', x=0, y=0, y_anchor='M')],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)
keyboard.extensions.append(display)

keyboard.keymap = [
    [KC.MPRV, KC.MNXT, KC.NO],  
    [KC.NO,   KC.NO,   KC.NO],  
    [KC.NO,   KC.Z,    KC.X]   
]
