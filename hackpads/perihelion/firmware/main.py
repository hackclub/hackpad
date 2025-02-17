
#   █▀█ █▀▀ █▀█ █ █░█ █▀▀ █░░ █ █▀█ █▄░█
#   █▀▀ ██▄ █▀▄ █ █▀█ ██▄ █▄▄ █ █▄█ █░▀█

# this is my custom macropad for hackclub's hackpad YSWS.
# its a simple, 4 button macropad with a OLED screen and RGB underglow, powered by a RP2040 microcontroller.

import board
import neopixel
import digitalio
import time
import busio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC, make_key
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#LEDS_COUNT = 7
#LED_PIN = board.A1
PURPLE = (128, 0, 128)
GREEN = (0, 255, 0)
OFF = (0, 0, 0)
MODE = "1"

rgb = RGB(
    pixel_pin=board.A1,  # GPIO27/ADC1/A1
    num_pixels=7,
    val_limit=100,
    val_default=100,
    animation_mode=AnimationModes.STATIC
)

CTRL_R = KC.LCTRL(KC.R)
CTRL_S = KC.LCTRL(KC.S)
CTRL_V = KC.LCTRL(KC.V)

KEYMAP_1 = [KC.Q, KC.W, KC.E, KC.R]  # QWER 
KEYMAP_2 = [KC.D, KC.F, KC.J, KC.K]  # DFJK
KEYMAP_3 = [KC.SPC, KC.LCTRL(KC.R), KC.LCTRL(KC.S), KC.LCTRL(KC.V)]  # Space Ctrl+R Ctrl+S Ctrl+V

@rgb.on.press()
def key_pressed(key, keyboard):
    global MODE
    keys = keyboard.active_keys
    
    if len(keys) == 4:
        rgb.set_pixel(4, GREEN)
        rgb.set_pixel(5, GREEN)
        rgb.set_pixel(6, GREEN)
        MODE = "3"
        keyboard.keymap = [KEYMAP_3]
    elif len(keys) == 3:
        rgb.set_pixel(4, GREEN)
        rgb.set_pixel(6, GREEN) # messed up LED order on the PCB, whoops
        MODE = "2"
        keyboard.keymap = [KEYMAP_2]
    elif len(keys) == 2:
        rgb.set_pixel(4, GREEN)
        MODE = "1"
        keyboard.keymap = [KEYMAP_1]
    else:
        if key == KC.Q:
            rgb.set_pixel(0, PURPLE)
        elif key == KC.W:
            rgb.set_pixel(1, PURPLE)
        elif key == KC.E:
            rgb.set_pixel(2, PURPLE)
        elif key == KC.R:
            rgb.set_pixel(3, PURPLE)

@rgb.on.release()
def key_released(key, keyboard):
    if key == KC.Q:
        rgb.set_pixel(0, OFF)
    elif key == KC.W:
        rgb.set_pixel(1, OFF)
    elif key == KC.E:
        rgb.set_pixel(2, OFF)
    elif key == KC.R:
        rgb.set_pixel(3, OFF)

keyboard.extensions.append(rgb)

oled = Oled(
    OledData(
        image_path="/gifs/Perihelion.gif", # GIFs need to be 128x32 to be displayed without any errors!!
    ),
    toDisplay=OledDisplayMode.IMG,
    flip=False,
)

keyboard.extensions.append(oled)

keyboard.keymap = [KEYMAP_1]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()