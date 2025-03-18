from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap, Delay
from kmk.extensions.led import LED
from kmk.extensions.led import AnimationModes

import board
import busio

print("Starting")

macros = Macros()


# class LayerTracker(RGB):
#     def on_layer_change(self, layer):
#         if layer == 0:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 0", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 1:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 1", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 2:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 2", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)
#         elif layer == 4:
#             display.entries = [
#                 ImageEntry(image="catswhite.bmp", x=0, y=0),
#                 TextEntry(text="Layer 1", x=64, y=32, x_anchor="B", y_anchor="M")
#             ]
#             keyboard.extensions.append(display)            # white

COL0 = board.D10
COL1 = board.D9
COL2 = board.D8
COL3 = board.D7
COL4 = board.D6

ROW0 = board.D3
ROW1 = board.D2
ROW2 = board.D1
ROW3 = board.D0





keyboard = KMKKeyboard()
layers = Layers()

col_pins = (COL0, COL1, COL2, COL3, COL4)
row_pins = (ROW0, ROW1, ROW2, ROW3)
keyboard.col_pins = col_pins
keyboard.row_pins = row_pins
diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(layers)
keyboard.modules.append(macros)

# led = LED(
#     led_pin=led_pin,
#     brightness=50,
#     brightness_step=5,
#     brightness_limit=100,
#     breathe_center=1.5,
#     animation_mode=AnimationModes.BREATHING,
#     animation_speed=1,
#     user_animation=None,
#     val=100,
#     )

keyboard.extensions.append(led)

# Layers
TOGGLE = KC.TG(1)

CONTROL_S_MACRO = KC.MACRO(
    Press(KC.RCTRL),
    Press(KC.S),
    Delay(500),
    Release(KC.RCTRL),
    Release(KC.S),
)

ALT_S = KC.RALT(KC.S) # Use for Slack - 1

ALT_T = KC.RALT(KC.T) # Use for Terminal - 2

ALT_F = KC.RALT(KC.F) # Use for Figma - 3

ALT_V = KC.RCALT(KC.V) # Use for Visual Studio Code - 4

# ALT_M = KC.RCALT(KC.M) # Use for Messages

ALT_C = KC.RCALT(KC.C) # Use for Canva - 5

ALT_X = KC.RCALT(KC.X) # Use for Xcode - 6

ALT_B = KC.RCALT(KC.B) # Use for Blender - 7

ALT_O = KC.RCALT(KC.O) # Use for OBS Studio - 8

# ALT_P = KC.RCALT(KC.P) # Use for Spotify

ALT_G = KC.RCALT(KC.G) # Use for Godot - 9

# ALT_L = KC.RCALT(KC.L) # Use for Flipper

# ALT_W = KC.RCALT(KC.W) # Use for Whiskey

# ALT_E = KC.RCALT(KC.E) # Use for Steam

# ALT_K = KC.RCALT(KC.K) # Use for KiCad

keyboard.keymap = [
    # Base Layer
    [
        KC.F13, KC.F16,         KC.F17, KC.F18,
        KC.F19,                         KC.F20,
                KC.F21, KC.F22, KC.F23,
                        TOGGLE,
    ],

    # Function Layer
    [
        ALT_S, ALT_T,        ALT_F, ALT_V,
        ALT_C,                      ALT_X,
               ALT_B, ALT_O, ALT_G,
                      TOGGLE,
    ],
]

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=driver,
    entries=[
        ImageEntry(image="catswhite.bmp", x=0, y=0),
    ]
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.8, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=20, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()