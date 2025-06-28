import board
import time
import math
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rotary_encoder import RotaryEncoderHandler

# Initialize keyboard
keyboard = KMKKeyboard()

# Define layers module
layers = Layers()
keyboard.modules.append(layers)

# Define rotary encoder module
encoder_handler = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler)

# Define keymap for 3x3 matrix
keyboard.keymap = [
    [KC.MRWD, KC.MPLY, KC.MFFD],  # Top row
    [KC.MSEL, KC.CALC, KC.LGUI(KC.R)],  # Middle row
    [KC.LEFT, KC.RIGHT, KC.LGUI(KC.L)],  # Bottom row
]

# Assign rotary encoder actions
encoder_handler.pins = (board.GP26, board.GP27)
encoder_handler.divisor = 4
encoder_handler.map = [KC.VOLD, KC.VOLU]  # Rotate Left = Volume Down, Rotate Right = Volume Up

# Define rotary encoder button
encoder_button = digitalio.DigitalInOut(board.GP28)
encoder_button.switch_to_input(pull=digitalio.Pull.UP)

# LED Mode Variables
led_modes = ["Solid", "Rainbow", "Wave", "Grid Fade"]
current_mode = 0

# Function to update LED effects
def update_leds():
    keyboard.leds.fill((0, 0, 0, 0))  # Clear LEDs

    if led_modes[current_mode] == "Solid":  # Actually a slow pulsing blue lol
        t = time.monotonic() * 1.5  # Anim speed
        for i, (x, y) in enumerate(keyboard.led_positions):
            wave = int((math.sin(t + x * 0.5 + y * 0.5) + 1) * 127)
            keyboard.leds[i] = (0, 0, wave, wave // 2)
    elif led_modes[current_mode] == "Rainbow":
        for i, (x, y) in enumerate(keyboard.led_positions):
            keyboard.leds[i] = (i * 18, 255 - i * 18, 0, 0)  # Rainbow effect
    elif led_modes[current_mode] == "Wave":  # Water flow effect with sin motion
        t = time.monotonic() * 2  # Anim speed
        for i, (x, y) in enumerate(keyboard.led_positions):
            wave_intensity = int((math.sin(t + (x * 0.8) + (y * 0.5)) + 1) * 127)
            keyboard.leds[i] = (0, wave_intensity // 2, wave_intensity, 0)
    elif led_modes[current_mode] == "Grid Fade": # Gentle pulsing effect, I was trying to mimic sunlight through water
        t = time.monotonic() * 1.2  # Anim speed
        for i, (x, y) in enumerate(keyboard.led_positions):
            brightness = int((math.sin(t + x + y) + 1) * 80)
            keyboard.leds[i] = (0, brightness // 2, brightness, 0)

    keyboard.leds.show()

# Main Loop for LED Mode Cycling
def handle_led_modes():
    global current_mode
    if not encoder_button.value:  # Button pressed
        time.sleep(0.2)  # Debounce
        current_mode = (current_mode + 1) % len(led_modes)  # Cycle modes
        update_leds()

if __name__ == "__main__":
    while True:
        keyboard.go()
        handle_led_modes()
        update_leds()
        time.sleep(0.1)
