import board
import time 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()

# Initialize the RGB matrix
rgb = Rgb_matrix()
keyboard.extensions.append(rgb)

keyboard.matrix = MatrixScanner(
    column_pins=[board.GP4, board.GP2, board.GP1],
    row_pins=[board.GP6, board.GP7, board.GP0],
    value_when_pressed=False,
)

keyboard.keymap = [
    # Layer 0
    [
        [KC.F13, KC.F14, KC.F15],
        [KC.F16, KC.F17, KC.F18],
        [KC.F19, KC.F20, KC.F21],
    ],
    # Layer 1
    [
        [KC.F13, KC.F23, KC.F24],
        [KC.F25, KC.F26, KC.F27],
        [KC.F28, KC.F29, KC.F30],
    ],
    # Layer 2
    [
        [KC.F13, KC.F32, KC.F33],
        [KC.F34, KC.F35, KC.F36],
        [KC.F37, KC.F38, KC.F39],
    ],
]

# Function to switch layers and control LEDs
def switch_layer(layer):
    keyboard.active_layers = [layer]
    if layer == 0:
        rgb.set_pixel(0, 255, 0, 0)  # Red for layer 0
        rgb.set_pixel(1, 0, 0, 0)    # Off for other LEDs
        rgb.set_pixel(2, 0, 0, 0)
    elif layer == 1:
        rgb.set_pixel(0, 0, 0, 0)    # Off for other LEDs
        rgb.set_pixel(1, 0, 255, 0)  # Green for layer 1
        rgb.set_pixel(2, 0, 0, 0)
    elif layer == 2:
        rgb.set_pixel(0, 0, 0, 0)    # Off for other LEDs
        rgb.set_pixel(1, 0, 0, 0)
        rgb.set_pixel(2, 0, 0, 255)  # Blue for layer 2
    rgb.write()

# Set initial layer and LED state
current_layer = 0
switch_layer(current_layer)

# Main loop to handle key events
while True:
    keyboard.update()
    if keyboard.matrix.is_pressed(0, 0):  # Check if the first key is pressed
        current_layer = (current_layer + 1) % 3  # Cycle through layers 0, 1, 2
        switch_layer(current_layer)
        time.sleep(0.3)  # Debounce delay    

if __name__ == '__main__':
    keyboard.go()
