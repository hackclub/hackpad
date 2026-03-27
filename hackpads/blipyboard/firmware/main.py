# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.mouse_keys import MouseKeys
from kmk.extensions.rgb import RGB
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, ImageEntry, TextEntry
from kmk.scanners.matrix import MatrixScanner


col1 = board.GP29
col2 = board.GP28
col3 = board.GP27
col4 = board.GP26
row1 = board.GP4
row2 = board.GP0
SDA = board.GP6
SCL = board.GP7
EC11A = board.GP2
EC11B = board.GP1

# This is the main instance of your keyboard
keyboard = KMKKeyboard()
mouse_keys = MouseKeys()
keyboard.extensions.append(mouse_keys)

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()

keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((EC11A, EC11B),)
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

rgb = RGB(pixel_pin=board.GP3, 
          num_pixels=8, 
          rgb_order=(1,0,2),
          
          )
keyboard.extensions.append(rgb)

i2c_bus = busio.I2C(SCL, SDA)
driver = SSD1306(i2c=i2c_bus)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=1, # initial screen brightness level
)

display.entries = [
    ImageEntry(image="me.bmp", x=0, y=0, layer=0),
]
keyboard.extensions.append(display)


# Define your pins here!
ROW_PINS = [row1, row2]
COL_PINS = [col1, col2, col3, col4]


keyboard.matrix = MatrixScanner(
    columns=COL_PINS,
    rows=ROW_PINS,
)

keyboard.keymap = [
    [
        KC.MPRV, KC.MPLY, KC.MNXT, MouseKeys.LEFT_BUTTON,
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.MACRO("jxcai534@gmail.com"), MouseKeys.LEFT_BUTTON,
    ]
]

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md


# Start kmk!
if __name__ == '__main__':
    keyboard.go()