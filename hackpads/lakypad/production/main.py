# LAKYPAD FIRMWARE v1.0.0
# BY LAKY2k8, 2025
############################################

import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(
    i2c=i2c_bus,
)

keyboard = KMKKeyboard();
macros = Macros(keyboard)
keyboard.modules.append(macros)

# OLED Display
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=64, # screen size
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

display.entries = [
	TextEntry("LakyPad v1.0.0", 0, 0),
	TextEntry("by Laky2k8 2025", 0, 10),

]
keyboard.extensions.append(display)

col_pins = (board.D1, board.D2, board.D3, board.D4) 
row_pins = (board.D11, board.D9, board.D7)
diode_orientation = DiodeOrientation.ROW4COL

keyboard.matrix = KeysScanner(keyboard, row_pins, col_pins, diode_orientation)

keys = [
	[KC.F17, KC.F18, KC.F19, KC.F20],
	[KC.F21, KC.F22, KC.F23, KC.F24],
	[KC.MACRO("LakyPad"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)), KC.MACRO("https://www.youtube.com/watch?v=xvFZjo5PgG0"), KC.MACRO("ffmpeg -i video.webm video.mp4")]
]

keyboard.keymap = keys

if __name__ == "__main__":

	keyboard.go()