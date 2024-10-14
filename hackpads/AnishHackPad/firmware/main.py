
# Main firmware script for keyboard setup using KMK
print("Starting keyboard firmware...")

# Basic imports for KMK and peripherals
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Additional modules
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB

# Initialize the keyboard
keyboard = KMKKeyboard()

# RGB setup (adjust the pin and number of LEDs)
rgb = RGB(pixel_pin=board.GP3, num_pixels=2)
keyboard.extensions.append(rgb)

# Rotary encoder setup
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP0, board.GP1, None, False))  # Modify pin A and B as required

keyboard.modules.append(encoder_handler)

# Keymap configuration (adjust key bindings as needed)
keyboard.keymap = [
    [
        KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP,  # Rotary encoder actions
        KC.F, KC.U, KC.C, KC.K,              # Key switches
    ]
]

if __name__ == '__main__':
    keyboard.go()  # Start the firmware
