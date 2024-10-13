from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.keys import KC
import board
import time
import math

keyboard = KMKKeyboard()

# Define the row and column pins
keyboard.matrix = [
    [26, 27, 28, 29, 0],   # Columns
    [3, 4, 2, 1]           # Rows
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC_C,  KC_D,  KC_E,  KC_F,  None],     # Row 0
    [KC_8,  KC_9,  KC_A,  KC_B,  KC_BSPC],  # Row 2
    [KC_4,  KC_5,  KC_6,  KC_7,  KC_X],     # Row 1
    [KC_0,  KC_1,  KC_2,  KC_3,  None]      # Row 3
]

RGB_PIN = board.GP6
NUM_PIXELS = 14

rgb = RGB (pin=RGB_PIN, num_leds=NUM_PIXELS)
keyboard.extensions.append(rgb)

def rainbow_cycle(wait):
    num_pixels = NUM_PIXELS
    for j in range(256):
        for i in range(num_pixels):
            
            pixel_index = (i * 256 // num_pixels) + j
            hue = pixel_index / 256.0
            
            rgb.set_hsvhsv_to_rgb(hue, 1.0, 1.0, i)
        rgb.show()
        time.sleep(wait)

# Start the keyboard
if __name__ == '__main__':
    while True:
        rainbow_cycle(0.05)
        keyboard.go()
