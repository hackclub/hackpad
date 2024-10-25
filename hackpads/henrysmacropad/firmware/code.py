import board
import digitalio
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.extensions.led import RGB
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.builtin import BuiltInDisplay
from adafruit_ssd1306 import SSD1306_I2C
from neopixel import NeoPixel

#init
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D3, board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D2, board.D1, board.D0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


#keymap
keyboard.keymap = [
    [KC.AUDIO_MUTE, KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.LALT(KC.F4)],
    [         KC.Q,                KC.D,                KC.C,                KC.G,           KC.G],
    [         KC.E,                KC.T,                KC.B,                KC.I,           KC.B],
]
keyboard.extensions.append(MediaKeys())

#LED shenanigans
pixels_pin = board.D6
pixels_num = 10
pixels = NeoPixel(pixels_pin, pixels_num, brightness=0.5, auto_write=False)
keyboard.extensions.append(RGB(pixel_pin=pixels_pin, num_pixels=pixels_num))

def update_pixels():
    pixels[0] = (255, 193, 14)
    pixels[1] = (83, 255, 15)
    pixels[2] = (247, 15, 255)
    for i in range(3, pixels_num):
        pixels[i] = (i * 40 % 255, 255 - (i * 40 % 255), (i * 20 % 255))
    pixels.show()

#oled
i2c_bus = busio.I2C(board.SCL, board.SDA)
oled = SSD1306_I2C(i2c=i2c_bus)
driver = BuiltInDisplay(
    display=board.DISPLAY,
    sleep_command=0xAE,
    wake_command=0xAF
)
display = Display(
    display=driver,
    width=128,
    height=64,
    brightness=0.8,
)
keyboard.extensions.append(display)

def display_oled():
    oled.fill(0)
    oled.text("among us sus", 0, 0, 1)
    oled.show()

    display.entries = [
        TextEntry(text="among us sus", x=0, y=0),
    ]

@keyboard.timer(50)
def periodic():
    display_oled()
    update_pixels()

keyboard.before_matrix_scan = periodic

if __name__ == '__main__':
    keyboard.go()
