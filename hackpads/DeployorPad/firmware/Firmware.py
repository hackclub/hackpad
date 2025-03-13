import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=[board.GP4, board.GP2, board.GP1],  # Columns
    row_pins=[board.GP28, board.GP29, board.GP6, board.GP7, board.GP0],  # Rows
    value_when_pressed=False,
)

# Define Keymap
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15,
        KC.F16, KC.F17, KC.F18,
        KC.F19, KC.F20, KC.F21,
        KC.F22, KC.F23, KC.F24,
        KC.MPRV, KC.MNXT, KC.MPLY,
    ]
]

encoder = RotaryEncoderHandler(pin_a=board.GP27, pin_b=board.GP26)
encoder.rotation_cw = KC.VOLU  # Volume Up
encoder.rotation_ccw = KC.VOLD  # Volume Down
keyboard.modules.append(encoder)

rgb = Rgb_matrix(pin=board.GP3, led_count=3)
keyboard.extensions.append(rgb)

rainbow_index = 0
last_press_time = 0

def update_leds():
    global rainbow_index, last_press_time
    current_time = time.monotonic()
    
    if keyboard.keys_pressed:
        rgb.set_rgb_fill((255, 0, 0))
        last_press_time = current_time
    elif encoder.encoder_moved:
        rgb.set_rgb_fill((0, 255, 0)) 
    else:
        rainbow_colors = [
            (255, 0, 0), (255, 127, 0), (255, 255, 0), 
            (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
        ]
        rgb.set_rgb_fill(rainbow_colors[rainbow_index % len(rainbow_colors)])
        rainbow_index += 1

    time.sleep(0.1) 

keyboard.update_hook = update_leds 

if __name__ == '__main__':
    keyboard.go()