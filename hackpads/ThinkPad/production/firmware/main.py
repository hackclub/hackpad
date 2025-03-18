#this is not complete as I have run out of time. The screen, encoder, rgb and status led should work, but I have not figured out the IO expander yet.
print("Starting")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.statusled import statusLED
from kmk.modules.encoder import EncoderHandler
from adafruit_pcf8574 import PCF8574A
from kmk.extensions.RGB import RGB
from kmk.extensions.display.ssd1306 import SSD1306

rgb = RGB(pixel_pin=board.GP2, num_pixels=16)
keyboard.extensions.append(rgb)

encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

try:
    i2c = busio.I2C(board.SCL, board.SDA)
except ValueError:
    print("Failed to initialize I2C")

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP10, board.GP9, board.GP8,), # encoder #1 
)

encoder_handler.map = [ 
    ((KC.UP, KC.DOWN),),    # Encoder 1: Standard
]

pcf = PCF8574A(i2c, address=0x38)

statusLED = statusLED(led_pins=[board.GP0, board.GP1, board.GP2])
keyboard.extensions.append(statusLED)
statusLED = statusLED(
    led_pin=led_pin,
    brightness=30,
    brightness_step=5,
    brightness_limit=100,
)

display.entries = [
    TextEntry(text="Layer = 1", x=0, y=0),
    TextEntry(text="Hello!", x=0, y=12),
]
keyboard.extensions.append(display)

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW



keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    keyboard.go()

