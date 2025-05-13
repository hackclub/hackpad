import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.Display import Display, TextEntry, DISPLAY_OLED
from kmk.extensions.Display.display_oled_sh1106 import DisplayOledSH1106

keyboard = KMKKeyboard()

display = Display(
    display_type=DISPLAY_OLED, 
    i2c_address=0x3C,
    i2c_bus=1, 
    flip=True,
)

text_entry = TextEntry("Press:", 0, 0)
display.entries.append(text_entry)
keyboard.extensions.append(display)

rgb = RGB(
    pixel_pin=board.GP1,
    num_pixels=12,
    animation_mode=AnimationModes.STATIC,
    animation_speed=1,
    brightness=100,
    rgb_order=(1, 0, 2),  
)
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.GP3, board.GP4, board.GP2)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

def on_key_press(key_number):
    text_entry.text = f"Key: {key_number}"
    pixels = [(0, 0, 0)] * 12
    pixels[key_number - 1] = (255, 255, 255)
    rgb.set_rgb_value(pixels)

HELLO_KEYS = []
for i in range(12):
    key_number = i + 1
    new_key = KC.NO.clone()
    new_key.after_press_handler(lambda n=key_number: on_key_press(n))
    new_key.text = f'Hello World {key_number}'
    HELLO_KEYS.append(new_key)

keyboard.keymap = [
    [
        HELLO_KEYS[0],  HELLO_KEYS[1],  HELLO_KEYS[2],
        HELLO_KEYS[3],  HELLO_KEYS[4],  HELLO_KEYS[5],
        HELLO_KEYS[6],  HELLO_KEYS[7],  HELLO_KEYS[8],
        HELLO_KEYS[9],  HELLO_KEYS[10], HELLO_KEYS[11],
    ]
]

if __name__ == '__main__':
    keyboard.go()