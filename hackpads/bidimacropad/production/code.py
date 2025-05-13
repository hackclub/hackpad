from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData

keyboard = KMKKeyboard()

# Pins Configuration
keyboard.col_pins = (26, 27, 28, 29)
keyboard.row_pins = (3, 4, 2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Layers Configuration
LAYER_GENERAL = 0
LAYER_BLENDER = 1
LAYER_NANO = 2
LAYER_SELECTOR = 3

layers = Layers()
keyboard.modules.append(layers)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Oled Configuration
oled_ext = Oled(
    OledData(
        corner_one="KMK Firmware",
        corner_two="Layer: General",
        corner_three="",
        corner_four=""
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=True
)
keyboard.extensions.append(oled_ext)

# Keymap Configuration
keyboard.keymap = [
    # General
    [
        KC_PWR, KC_SLEP, KC_WAKE, KC_MUTE,
        KC_VOLU, KC_VOLD, KC_MNXT, KC_MPRV,
        KC_MSTP, KC_MPLY, KC_MSEL, KC_MO(LAYER_SELECTOR),
    ],
    # Blender
    [
        send_string('G'), send_string('S'), send_string('R'), send_string('E'),
        send_string('Ctrl+B'), send_string('Shift+D'), send_string('X'), send_string('Tab'),
        send_string('Ctrl+Z'), send_string('Ctrl+Shift+Z'), send_string('Shift+S'), KC.MO(LAYER_SELECTOR),
    ],
    # Nano
    [
        send_string('Ctrl+X'), send_string('Ctrl+C'), send_string('Ctrl+V'), send_string('Ctrl+S'),
        send_string('Ctrl+O'), send_string('Ctrl+W'), send_string('Ctrl+G'), send_string('Ctrl+T'),
        send_string('Ctrl+K'), send_string('Ctrl+J'), send_string('Ctrl+U'), KC.MO(LAYER_SELECTOR),
    ],
    # Layer Selector
    [
        KC.TO(LAYER_GENERAL), KC.TO(LAYER_BLENDER), KC.TO(LAYER_NANO), KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.TRNS,
    ],
]

# Encoder Configuration
encoder_handler.pins = ((0, 1),)
encoder_handler.map = (
    ((KC.LT(LAYER_SELECTOR, KC.NO), KC.LT(LAYER_SELECTOR, KC.NO)),),
)

def update_oled(layer):
    layer_names = ["General", "Blender", "Nano", "Selector"]
    oled_ext.data.corner_two = f"Layer: {layer_names[layer]}"

keyboard.before_matrix_scan = lambda: update_oled(layers.active_layer)

if __name__ == '__main__':
    keyboard.go()
