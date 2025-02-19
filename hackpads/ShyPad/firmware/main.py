import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display
from kmk.extensions.display.ssd1306 import SSD1306
import busio
import time

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers_ext = Layers()

keyboard.modules.append(encoder_handler)
keyboard.modules.append(layers_ext)
keyboard.extensions.append(MediaKeys())

i2c_bus = busio.I2C(board.D4, board.D5)
display = Display(
    SSD1306(
        width=128,
        height=32,
        i2c=i2c_bus,
        addr=0x3C,
        rotation=180,
        dim_time=10,
        dim_target=0.2,
        off_time=1200,
        brightness=1,
    )
)
keyboard.extensions.append(display)

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D5, board.D6, board.D7, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Layer 0 (Keypad)
    [
        KC.N0, KC.DOT, KC.TG(1),
        KC.N7, KC.N8,  KC.N9,
        KC.N4, KC.N5,  KC.N6,
        KC.N1, KC.N2,  KC.N3
    ],
    
    # Layer 1 (Extra Stuff)
    [
        KC.PRINT_SCREEN,  KC.TRNS,  KC.TRNS,
        KC.TRNS,          KC.TRNS,  KC.TRNS,
        KC.TRNS,          KC.UP,    KC.TRNS,
        KC.LEFT,          KC.DOWN,  KC.RIGHT
    ]
]

encoder_handler.pins = ((board.D9, board.D10, board.D6),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
    ((KC.LEFT, KC.RIGHT),),
]

def render_display(display):
    display.clear()

    active_layer = keyboard.active_layers[0] if keyboard.active_layers else 0
    layer_str = "Layer: {}".format(active_layer)

    current_time = time.localtime()
    time_str = "{:02d}:{:02d}:{:02d}".format(current_time[3], current_time[4], current_time[5])

    display.text(layer_str, 0, 0, 1)
    display.text(time_str, 0, 10, 1)
    display.show()


def on_runtime():
    render_display(display)

keyboard.before_matrix_scan.append(on_runtime)

if __name__ == '__main__':
    keyboard.go()
