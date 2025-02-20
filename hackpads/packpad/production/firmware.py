# quick firmware for my packpad (hackpad PACKED with features :D)
# by j4y_boi

print("starting da EPIKEST KEYBOARDDD >:D")

import board
import busio
import displayio
import digitalio
import terminalio
import rotaryio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.stock import simplekey
from kmk.extensions.media_keys import MediaKeys

from adafruit_display_text import label
import adafruit_displayio_ssd1306

keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [ #ill add something else later, hopefully
    [KC.N1, KC.N2, KC.N3],
    [KC.N4, KC.N5, KC.N6],
    [KC.N7, KC.N8, KC.N9],
    [KC.NO, KC.N0, KC.NO]
]

# tbh i dunno what i'm doing with the rotary encoder, I HOPE that the docs weren't lying
encoder = rotaryio.IncrementalEncoder(board.GP26, board.GP27)
last_position = None

displayio.release_displays()
i2c = busio.I2C(board.GP6, board.GP7)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# i dunno what to add on the screen lool
splash = displayio.Group()
text = "Is the display on?: I dunno probably"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=10, y=15)
splash.append(text_area)
display.show(splash)

def knobcheck():
    global last_position
    position = encoder.position

    if last_position is None:
        last_position = position

    if position > last_position:
        keyboard.tap_key(KC.VOLU)
    elif position < last_position:
        keyboard.tap_key(KC.VOLD)

    last_position = position

# key board enable >:0
if __name__ == '__main__':
    keyboard.go()
    while True: #i think this is how it works
        knobcheck()
