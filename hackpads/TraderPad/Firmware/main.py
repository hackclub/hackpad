from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeyMatrix
from kmk.handlers.sequences import send_string
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.matrix = KeyMatrix(rows=(7, 8, 9), cols=(3, 4, 5, 6))
layers = Layers()
keyboard.modules.append(layers)

rgb = RGB(pixel_pin=10, num_pixels=4, rgb_order=(1, 0, 2))
keyboard.extensions.append(rgb)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.extensions.append(MediaKeys())

LAYER_1 = (
    KC.NLCK, KC.P7, KC.P8, KC.P9,
    KC.PPLS, KC.P4, KC.P5, KC.P6,
    KC.PMNS, KC.P1, KC.P2, KC.P3,
)

LAYER_2 = (
    KC.ESC, KC.Q, KC.W, KC.E,
    KC.R, KC.A, KC.S, KC.D,
    KC.F, KC.Z, KC.X, KC.C,
)

LAYER_3 = (
    KC.F1, KC.F2, KC.F3, KC.F4,
    KC.F5, KC.F6, KC.F7, KC.F8,
    KC.F9, KC.F10, KC.F11, KC.F12,
)

LAYER_4 = (
    KC.MPLY, KC.MPRV, KC.MNXT, KC.MUTE,
    KC.VOLD, KC.VOLU, KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP,
    KC.NO, KC.NO, KC.NO, KC.NO,
)

keyboard.keymap = [LAYER_1, LAYER_2, LAYER_3, LAYER_4]

encoder_handler.pins = ((0, 1),) 
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU), (KC.TRNS, KC.TRNS)),
]


layer_colors = [
    (0, 255, 100),    # red
    (85, 255, 100),   # green
    (170, 255, 100),  # nlue
    (42, 255, 100),   # yellow
]

active_layer = 0 

def update_leds():
    global active_layer
    rgb.set_hsv_fill(layer_colors[active_layer])


def switch_layer():
    global active_layer
    active_layer = (active_layer + 1) % 4
    layers.set_layer(active_layer)
    update_leds()

keyboard.add_hotkey((2,), switch_layer) 

update_leds()

if __name__ == '__main__':
    keyboard.go()
