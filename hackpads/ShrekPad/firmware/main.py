import os
import board
import digitalio
import busio
import displayio
import terminalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()

displayio.release_displays()
i2c = busio.I2C(board.GP5, board.GP4)  
display = SSD1306_I2C(128, 32, i2c)
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="Shrek is love, Shrek is life.", x=0, y=10)
splash.append(text_area)
display.show(splash)

def open_app(app_name):
    os.system(f'open -a "{app_name}"')

key_pins = [board.GP0, board.GP1, board.GP2]

keymap = [
    lambda: open_app("Visual Studio Code"),  
    lambda: (open_app("Discord"), open_app("WhatsApp")),  
    lambda: open_app("Spotify"),  
]

keyboard.keymap = [[keymap[i] for i in range(3)]]

while True:
    keyboard.go()
