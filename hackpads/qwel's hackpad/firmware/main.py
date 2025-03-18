from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.rotary_encoder import RotaryEncoder
from kmk.extensions.rgb import RGB
from kmk.extensions.led import LED
from kmk.modules.i2c_expander import PCF8574
import board

keyboard = KMKKeyboard()

# Set up the PCF8574 I/O Expander
i2c_expander = PCF8574(i2c=board.I2C(), address=0x20)

# Setup the Rotary Encoders
encoder1 = RotaryEncoder(pin_a=board.D3, pin_b=board.D4, divisor=4)
encoder2 = RotaryEncoder(pin_a=board.D5, pin_b=board.D6, divisor=4)

keyboard.modules.append(i2c_expander)
keyboard.modules.append(encoder1)
keyboard.modules.append(encoder2)

# Set up NeoPixel LEDs for gradient effect
rgb_ext = RGB(pixel_pin=board.D21, num_pixels=12, hue_default=0, sat_default=255, val_default=100)
keyboard.extensions.append(rgb_ext)

# Encoder Actions
@encoder1.on_step
def encoder1_turn(direction):
    if direction > 0:
        keyboard.tap_key(KC.VOLU)  # Volume Up
    else:
        keyboard.tap_key(KC.VOLD)  # Volume Down

@encoder2.on_step
def encoder2_turn(direction):
    if direction > 0:
        keyboard.tap_key(KC.BRIU)  # Brightness Up (Windows shortcut)
    else:
        keyboard.tap_key(KC.BRID)  # Brightness Down (Windows shortcut)

# Define keymap
keyboard.keymap = [
    # Row 0
    [KC.LWIN(KC.CMD), KC.LWIN(KC.L), KC.TASK],   # Open Command Prompt, Lock Screen, Task Manager
    # Row 1
    [KC.MUTE, KC.MPLY, KC.SCR],                  # Mute/Unmute, Play/Pause, Screenshot
    # Row 2
    [KC.CALC, KC.NOTEPAD, KC.DIR],               # Open Calculator, Notepad, Downloads Folder
    # Row 3
    [KC.CAL, KC.RGB_TOG, KC.FSCR],               # Open Calendar, Toggle RGB Gradient, Toggle Full-Screen
]

# Define RGB Gradient function (key KC.RGB_TOG)
rgb_gradient_idx = 0
gradient_colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]

def change_rgb_gradient():
    global rgb_gradient_idx
    rgb_gradient_idx = (rgb_gradient_idx + 1) % len(gradient_colors)
    rgb_ext.set_hsv(*gradient_colors[rgb_gradient_idx])

keyboard.process_key_toggled(KC.RGB_TOG, change_rgb_gradient)

if __name__ == '__main__':
    keyboard.go()
