import os
import board
import digitalio
import busio
import displayio
import terminalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from adafruit_display_text import label
from adafruit_ssd1306 import SSD1306_I2C

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

displayio.release_displays()
i2c = busio.I2C(board.GP5, board.GP4)  
display = SSD1306_I2C(128, 32, i2c)
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="Ready", x=0, y=10)
splash.append(text_area)
display.show(splash)

def update_display(text):
    text_area.text = text
    display.show(splash)

def open_premiere():
    os.system('open -a "Premiere Pro"')
    update_display("VS Code Opened")

def open_discord():
    os.system('open -a "Discord"')
    update_display("Discord Opened")

def open_spotify():
    os.system('open -a "Spotify"')
    update_display("Spotify Opened")

ROWS = [board.GP0, board.GP1, board.GP2, board.GP3]
COLS = [board.GP4, board.GP5, board.GP6]

keyboard.matrix = KeysScanner(
    rows=ROWS,
    cols=COLS,
    value_when_pressed=False,
)

keymap = [
    [lambda: open_premiere(), lambda: open_discord(), lambda: open_spotify()],
    [lambda: update_display("App 4 Opened"), lambda: update_display("App 5 Opened"), lambda: update_display("App 6 Opened")],
    [lambda: update_display("App 7 Opened"), lambda: update_display("App 8 Opened"), lambda: update_display("App 9 Opened")],
    [lambda: update_display("App 0 Opened"), lambda: update_display("ENTER"), lambda: update_display("ESC.")],
]

keyboard.keymap = keymap

while True:
    keyboard.go()
