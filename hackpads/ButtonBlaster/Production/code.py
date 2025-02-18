import board
import digitalio
import busio
import adafruit_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

i2c = busio.I2C(board.SCL, board.SDA)
oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 32
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, reset=oled_reset)

class Keyboard(KMKKeyboard):
    pass

keyboard = Keyboard()

keyboard.matrix = [
    [board.D10, board.D9, board.D8, board.D7],
    [board.D0, board.D1, board.D2],
    DiodeOrientation.COLUMNS
]

keyboard.keymap = [
    [KC.Q,  KC.W,  KC.E,  KC.R],  
    [KC.A,  KC.S,  KC.D,  KC.F],  
    [KC.SPC, KC.C,  KC.V,  KC.LSFT] 
]

def display_key(key):
    oled.fill(0)
    oled.text(f"Key: {key}", 0, 0)
    oled.show()

@keyboard.on_key
def handle_keypress(keycode, pressed):
    if pressed:
        display_key(keycode.name)

if __name__ == '__main__':
    keyboard.go()
