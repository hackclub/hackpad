print("Starting")

# import modules
import board
import busio
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from adafruit_pcf8574 import PCF8574A

# init i2c
try:
    i2c = busio.I2C(board.SCL, board.SDA)
except ValueError:
    print("Failed to initialize I2C")

# display configuration
driver = SSD1306(
    i2c=i2c,
    device_address=0x3C,
)

# init keyboard and modules
keyboard = KMKKeyboard()
layers = Layers()
macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler, macros]

# init PCF8574A i/o expander
pcf = PCF8574A(i2c, address=0x38)

# encoder configuration
encoder_handler.pins = (
    (pcf.get_pin(4), pcf.get_pin(6),),  # encoder #1 (regular direction)
    (pcf.get_pin(5), pcf.get_pin(7), None, True, 2,),  # encoder #2 (reversed direction, divisor 2)
)

# display setup
display = Display(
    display=driver,
    entries=[    
        TextEntry(text="Layer = 1", x=0, y=0),
        TextEntry(text="Macros", x=0, y=12),
        TextEntry(text="Hey there!", x=0, y=24),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

# macropad matrix configuration
keyboard.col_pins = (board.GP1, board.GP2, board.GP4)
keyboard.row_pins = (board.GP26, board.GP27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# macro definition
PARROT = KC.MACRO(
    KC.LWIN,
    KC.R,
    KC.MACRO_SLEEP_MS(700),
    "cmd",
    KC.MACRO_SLEEP_MS(700),
    KC.ENTER,
    KC.MACRO_SLEEP_MS(1200),
    "curl parrot.live",
    KC.MACRO_SLEEP_MS(700),
    KC.ENTER,
    KC.MACRO_SLEEP_MS(1500),
)

# keymap
keyboard.keymap = [
    # Layer 0: Base layer
    [
        KC.TO(1),   PARROT,     PARROT,     KC.MUTE,
        PARROT,     KC.R,       KC.T,       KC.MUTE,
    ],
    # Layer 1: Function Layer
    [
        KC.TO(0),   KC.F1,      KC.F2,     KC.MUTE,
        KC.F3,      KC.F4,      KC.F5,     KC.MUTE,
    ],
]

# encoder mapping
encoder_handler.map = [ 
    ((KC.UP, KC.DOWN),),    # Encoder 1: Standard
    ((KC.LEFT, KC.RIGHT),), # Encoder 2: Reversed
]

# add display to extensions
keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()
