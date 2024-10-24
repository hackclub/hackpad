from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoder
from kmk.modules.holdtap import HoldTap
from kmk.extensions.string import send_string
from kmk.handlers.sequences import simple_key_sequence
import supervisor
import board
import digitalio
import time

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

# Define rotary encoders with correct XIAO RP2040 pins
encoder_left.pins = (board.D9, board.D10)  # Volume control
encoder_right.pins = (board.P1, board.P2)  # Side scroll with shift

encoder_left.rotation_action = [KC.VOLU, KC.VOLD]  # Volume control
encoder_right.rotation_action = [KC.LSFT(KC.WH_U), KC.LSFT(KC.WH_D)]  # Side scroll

# Key matrix pin setup with correct XIAO RP2040 pins
keyboard.row_pins = (board.D6, board.D7, board.P0)  # Rows from top to bottom
keyboard.col_pins = (board.D3, board.D4, board.D5)  # Columns from left to right
keyboard.diode_orientation = 0  # Standard diode orientation

# Track the hold state of the top three buttons and their hold start time
top_buttons_held = [False, False, False]
hold_start_time = None
HOLD_TIME_THRESHOLD = 3  # 3 seconds

# Check if all top three buttons are held
def check_all_top_buttons_held():
    return all(top_buttons_held)

# Function to switch layers
def switch_layer(new_layer):
    keyboard.active_layers = [new_layer]
    control_led_based_on_layer(new_layer)

# Custom function to handle button hold detection
def process_top_button_hold(idx, pressed):
    global top_buttons_held, hold_start_time
    top_buttons_held[idx] = pressed

    if check_all_top_buttons_held():
        if hold_start_time is None:
            hold_start_time = time.monotonic()  # Start timing
    else:
        hold_start_time = None  # Reset the timer if any button is released

# Layer switch check based on button hold time
def check_layer_switch():
    global hold_start_time
    if hold_start_time and (time.monotonic() - hold_start_time) >= HOLD_TIME_THRESHOLD:
        # Switch layers when the threshold is reached
        current_layer = keyboard.active_layers[0]
        new_layer = DAVINCI if current_layer == DEFAULT else DEFAULT
        switch_layer(new_layer)
        hold_start_time = None  # Reset hold time after switching

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

# LED control for indicating active layer
led_pin = board.P3  # Set the pin where the LED is connected
pin_led = digitalio.DigitalInOut(led_pin)
pin_led.direction = digitalio.Direction.OUTPUT

# Function to turn the LED on or off based on active layer
def control_led_based_on_layer(layer):
    if layer == DAVINCI:  # DaVinci Resolve layer
        pin_led.value = True  # Turn on the LED
    else:
        pin_led.value = False  # Turn off the LED

if __name__ == '__main__':
    # Main loop
    while True:
        check_layer_switch()  # Check for layer switch condition
        keyboard.go()  # Run the keyboard loop
