import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.led import LED
from kmk.modules.neopixel import Neopixel
from kmk.modules.oled import OLED # the .96 screen oled one urrent ly for led toggle later for the keypad togggle,

keyboard = KMKKeyboard()

# thisis the rp2040 pins used the both diode and key ones from 2-5 and 8-11
MATRIX_PINS = [
    (board.GP2, board.GP3, board.GP4, board.GP5),  # Rows
    (board.GP8, board.GP9, board.GP10, board.GP11),  # Columns
]

NEOPIXEL_PIN = board.GP1  # 1 ist pin to send dta to leds

OLED_SCL = board.GP6  
OLED_SDA = board.GP7  # OLED 2 extra pins btwn dnd vcc


led = LED()
keyboard.modules.append(led)

neopixel = Neopixel(
    pin=NEOPIXEL_PIN, n=9, brightness=0.5, auto_write=False
)
keyboard.modules.append(neopixel)

oled = OLED(
    scl=OLED_SCL,
    sda=OLED_SDA,
    width=128,
    height=32,
)
keyboard.modules.append(oled)


keyboard.matrix = KeysScanner(
    pins=MATRIX_PINS,
    value_when_pressed=False,
)

# here are the gaming keys for gamepad lets hope thses will be what is needed and i dont need more as i saw these to be mosr comon
KC_GAME_1 = KC.W
KC_GAME_2 = KC.A
KC_GAME_3 = KC.S
KC_GAME_4 = KC.D # main gaming keys for movment
KC_GAME_5 = KC.ESC
KC_GAME_6 = KC.LSHIFT
KC_GAME_7 = KC.LCTRL
KC_GAME_8 = KC.LALT
KC_GAME_9 = KC.ENTER #rest mist imp kys
KC_GAME_10 = KC.Q  
KC_GAME_11 = KC.E  
KC_GAME_12 = KC.R  

KC_TOGGLE_COLOR = KC.NO  

#this is gaming layout but i diont think ill agree thus will need to change the keys to suit my needs
keyboard.keymap = [
    [
        KC_GAME_5, KC_GAME_6, KC.TAB, KC.LALT,  # ESC Shift Tab Alt addd here as wad need to be in middle for me to use confortably
        KC_GAME_1, KC_GAME_2, KC_GAME_3, KC_GAME_4,  # W A S D main keys
        KC_GAME_9, KC_GAME_10, KC_GAME_11, KC_GAME_12,  # Enter and rest keys
        KC_TOGGLE_COLOR, KC.LCTRL, KC.NO, KC.NO,  # Toggle Color + Ctrl + Extra #13th key to change color lo leds neopixls
    ]
]

current_color_index = 0
colors = [ 
    (255, 0, 0),  # Red color
    (0, 255, 0),  # Green colour
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 255, 255),  # White color -added 5 for now will work on more when i get time deadline is too close
]

def set_neopixel_color(color):
    for i in range(9):  # 9 Neopixels i used hpe theyll run i added capicitor(100uf) lets see shouldnt cause errors
        neopixel.set_pixel(i, color)
    neopixel.show()

# Sets the first color for leds
set_neopixel_color(colors[current_color_index])


def process_key(key, pressed):
    global current_color_index
    if key == KC_TOGGLE_COLOR and pressed:
        current_color_index = (current_color_index + 1) % len(colors)  # Cycles through colors on key 13 top togle wil later be used to toggle to numpad once i learn kmk
        set_neopixel_color(colors[current_color_index])
        return True  
    return False

def oled_task():
    oled.clear()
    oled.write_line("Gaming Keypad")
    # Corrected OLED display to show the color addd above on togle change
    oled.write_line(f"Color: RGB({colors[current_color_index][0]}, {colors[current_color_index][1]}, {colors[current_color_index][2]})")
    oled.show()

keyboard.process_key = process_key
keyboard.oled_task = oled_task

if __name__ == "__main__":
    keyboard.go()
