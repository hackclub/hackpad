# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extension.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D6, board.D10, board.D9)
keyboard.row_pins = (board.D7, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D2, board.D1, None, False),)

#OLED Display
i2c_bus = busio.I2C(board.D_SCL, board.D_SDA)

display_driver = SSD1306(
    i2c=i2c_bus
)

display = Display(
    display=display_driver,
    entries=[
        #will add display content when i receive the hackpad
    ],
    width=128
    height=32
    dim_time=10
    dim_target=0.2
    off_time=1200
    brightness=1
)

#Macros
PRINT = simple_key_sequence(
    (
        KC.LCTL(KC.P),
    )
)
SAVE = simple_key_sequence(
    (
        KC.LCTL(KC.S)
    )
)
COPY = simple_key_sequence(
    (
        KC.LCTL(KC.C)
    )
)
PASTE = simple_key_sequence(
    (
        KC.LCTL(KC.V)
    )
)



#Keymap
keyboard.keymap = [
    [COPY, PASTE, SAVE, PRINT,
     KC.PSCR, KC.PAUS, KC.NO, KC.MUTE #may change this or add more layers when i receive the hackpad
    ]
]

#Encoder
encoder_handler.map = [ 
    (
        (KC.UP, KC.DOWN),
    ),
]

#Start
if __name__ == '__main__':
    keyboard.go()