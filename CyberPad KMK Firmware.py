from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoder
from kmk.modules.holdtap import HoldTap
from kmk.extensions.string import send_string
from kmk.handlers.sequences import simple_key_sequence
import supervisor

keyboard = KMKKeyboard()

# Add layers and HoldTap modules
layers_ext = Layers()
keyboard.modules.append(layers_ext)
ht = HoldTap()
keyboard.modules.append(ht)

# Add rotary encoder module
encoder_left = RotaryEncoder()
encoder_right = RotaryEncoder()
keyboard.modules.append(encoder_left)
keyboard.modules.append(encoder_right)

# Define layers
DEFAULT = 0
DAVINCI = 1

# Define rotary encoders
encoder_left.pins = (9, 10)  # Volume control
encoder_right.pins = (1, 2)  # Side scroll with shift

encoder_left.rotation_action = [KC.VOLU, KC.VOLD]  # Volume control
encoder_right.rotation_action = [KC.LSFT(KC.WH_U), KC.LSFT(KC.WH_D)]  # Side scroll

# Key matrix pin setup
keyboard.row_pins = (6, 7, 8)  # Rows from top to bottom
keyboard.col_pins = (3, 4, 5)  # Columns from left to right
keyboard.diode_orientation = 0  # Standard diode orientation

# Track the hold state of the top three buttons
top_buttons_held = [False, False, False]

# Check if all top three buttons are held
def check_all_top_buttons_held():
    return all(top_buttons_held)

# Custom function to handle button hold detection
def process_top_button_hold(idx, pressed):
    global top_buttons_held
    top_buttons_held[idx] = pressed
    if check_all_top_buttons_held():
        keyboard.active_layers = [DAVINCI]  # Switch to DaVinci layer
    else:
        keyboard.active_layers = [DEFAULT]  # Revert to Default layer

keyboard.keymap = [
    # Default layer (Media controls and system actions)
    [
        KC.HOLD_TAP(KC.MRWD, lambda: process_top_button_hold(0, True), lambda: process_top_button_hold(0, False)),  # Top left
        KC.HOLD_TAP(KC.MPLY, lambda: process_top_button_hold(1, True), lambda: process_top_button_hold(1, False)),  # Top middle
        KC.HOLD_TAP(KC.MFFD, lambda: process_top_button_hold(2, True), lambda: process_top_button_hold(2, False)),  # Top right
        KC.MPRV, KC.MNXT, KC.MSTP,  # Middle row
        KC.MUTE, KC.WIN_CALC, KC.LGUI(KC.L)  # Bottom row (Mute, Calculator, Lock Screen)
    ],

    # DaVinci Resolve layer (hotkeys for DaVinci Resolve)
    [
        KC.M(1), KC.M(2), KC.M(3),  # Top row: DaVinci hotkeys
        KC.M(4), KC.M(5), KC.M(6),  # Middle row: DaVinci hotkeys
        KC.MUTE, KC.M(7), KC.LGUI(KC.L)  # Bottom row: Mute, DaVinci hotkey, Lock Screen
    ]
]

# Custom macro function for opening Windows Calculator (used in KC.WIN_CALC)
def win_calc():
    send_string(KC.LGUI('r'))
    send_string('calc\n')

keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()
