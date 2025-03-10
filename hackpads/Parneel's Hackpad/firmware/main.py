print("Starting")

import board
import busio

from datetime import datetime

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys

from kmk.extensions.display import Display, SSD1306, TextEntry
# TODO: install display libraries on rp2040


# TODO: add layers for macro stuff and encoder

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Initialize OLED - SSD1306 0.91" 128x32
driver = SSD1306(i2c = busio.I2C(board.GP_SCL, board.GP_SDA))

oled = Display( # see kmk docs for extra params like brightness
  display=driver,
  entries = [
    TextEntry(text=datetime.now().strftime('%r'), x=0, y=0) # temp
  ]
)
keyboard.extensions.append(oled)

# Inititalize mouse keys
keyboard.modules.append(MouseKeys()) # note: the settings for this can be adjusted

# Encoder stuff
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP29, board.GP0, None))
encoder_handler.map = [
  ((KC.MW_UP, KC.MW_DOWN)) # add KC.NO to account for button if it crashes
]

# Note: this keymap is temporary and will be changed to do 
# actually useful things once I actually get the macropad

e = KC.E

keyboard.keymap = [
  [
    e, e, e, e,
    e, e, e, e,
    e, e, e, e
    ]
]

if __name__ == '__main__':
    keyboard.go()