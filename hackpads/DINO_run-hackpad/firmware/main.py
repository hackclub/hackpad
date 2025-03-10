import board
import digitalio
import busio
import displayio

#ssd1306 driver adafruit
import adafruit_displayio_ssd1306

from kmk.kmk.kmk_keyboard import KMKKeyboard
from kmk.kmk.keys import KC

#pin scanner
class DirectPinScanner:
    """
    returns 2D list
      True = key NOT pressed
      False = key pressed
    """
    def __init__(self, pins):
        self.pins = []
        for p in pins:
            d = digitalio.DigitalInOut(p)
            d.direction = digitalio.Direction.INPUT
            d.pull = digitalio.Pull.UP
            self.pins.append(d)

    def scan(self):
        return [[pin.value for pin in self.pins]]


displayio.release_displays()

#SCL: D5             SDA: D4
i2c = busio.I2C(board.D5, board.D4)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 64

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

#load DINO
try:
    bmp = displayio.OnDiskBitmap("dino.bmp")
    tile_grid = displayio.TileGrid(bmp, pixel_shader=bmp.pixel_shader)
    group = displayio.Group()
    group.append(tile_grid)
    display.show(group)
except Exception as e:
    print("Error loading dino:", e)


KEY_PINS = [
    board.D7,
    board.D8,
    board.D9,
    board.D1,
    board.D0,
    board.D2,
    board.D3,
    board.D6,
]

#create the keyboard and assign direct pin scanner.
keyboard = KMKKeyboard()
keyboard.matrix = DirectPinScanner(KEY_PINS)


keyboard.keymap = [
    [KC.N9, KC.N0, KC.LBRACKET, KC.RBRACKET, KC.TAB, KC.BSPACE, KC.ENTER, KC.SCOLON]
]

if __name__ == '__main__':
    keyboard.go()
