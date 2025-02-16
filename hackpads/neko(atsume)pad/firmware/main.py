import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display
from kmk.extensions.display.ssd1306 import SSD1306
import time

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

# Display setup
display = Display(
    SSD1306(
        width=128,
        height=32,
        i2c=board.I2C(),
        addr=0x3C,
        rotation=180,
    )
)
keyboard.extensions.append(display)

keyboard.col_pins = (board.PA02, board.PA04, board.PA10)
keyboard.row_pins = (board.PA11, board.PB08, board.PB09, board.PA07)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.N7,    KC.N8,   KC.N9,
        KC.N4,    KC.N5,   KC.N6,
        KC.N1,    KC.N2,   KC.N3,
        KC.N0,    KC.DOT,  KC.ENTER
    ]
]

# Rotary encoder setup
encoder_handler.pins = ((board.PA6, board.PA5, board.PA4),)

def encoder_handler(direction):
    if direction == 1:
        keyboard.tap_key(KC.VOLU)
    else:
        keyboard.tap_key(KC.VOLD)

encoder_handler.map = [(encoder_handler,)]

# OLED display function (untested, waiting for display and idk to arrive)
def render_time(display):
    display.clear()
    current_time = time.localtime()
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])
    display.text(time_str, 0, 0, 1)
    display.show()

def on_runtime():
    render_time(display)

keyboard.before_matrix_scan.append(on_runtime)

#todo: add layers for macros based on rotary encoder switch button.

if __name__ == '__main__':
    keyboard.go()