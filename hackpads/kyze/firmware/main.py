import busio
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()


COL0 = board.GP1
COL1 = board.GP0
COL2 = board.GP9
COL3 = board.GP6

ROW0 = board.GP3
ROW1 = board.GP2
ROW2 = board.GP10

# Rotary encoder pins
ROTA = board.GP8
ROTB = board.GP7

# display   
i2c = busio.I2C(board.GP_SCL, board.GP_SDA)

# Matrix settings: define rows, columns, and diode orientation
keyboard.col_pins = (COL0, COL1, COL2, COL3)  # 4 columns
keyboard.row_pins = (ROW0,ROW1, ROW2)  # 3 rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW   

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, None))
encoder_handler.map = (((KC.VOLD, KC.VOLU,),),) # KC.MUTE


keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LALT(KC.TAB), KC.MUTE],  # Row 1
    [KC.LALT(KC.Z), KC.LCTRL(KC.Y), KC.LCTRL(KC.S),],  # Row 2
    [KC.LALT(KC.R), KC.LCTRL(KC.T), KC.LCTRL(KC.W),],  # Row 2
]



driver = SSD1306(i2c=i2c, device_address=0x3C)
display = Display(
    display=driver,
    width=128,
    height=64,
    brightness=1,
    entries=[
        TextEntry(text="Kyze", x=0, y=0, y_anchor='K'),
        TextEntry(text="*##  Aarav  ##", x=15, y=15, y_anchor='r'),
    ]
)

if __name__ == '__main__':
    keyboard.go()
