import board
import displayio
import adafruit_displayio_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.oled import Oled
from kmk.modules.media_keys import MediaKeys
import adafruit_imageload
import time

keyboard = KMKKeyboard()

keyboard.col_pins = [board.D7, board.D8, board.D9, board.D10]

encoder = EncoderHandler()
keyboard.modules.append(encoder)

displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

sprite_sheet, palette = adafruit_imageload.load("/cp_sprite_sheet.bmp", bitmap=displayio.Bitmap, palette=displayio.Palette)
tile_grid = displayio.TileGrid(sprite_sheet, pixel_shader=palette, width=1, height=1, tile_width=32, tile_height=32)
group = displayio.Group()
group.append(tile_grid)

display.show(group)

def animate():
    for frame in range(6):
        tile_grid[0] = frame
        display.refresh()

keymap = [
    [
        KC.MACRO('git commit -am "."'),
        KC.MACRO('git push --force'),
        KC.MACRO('git pull'),
        KC.MACRO('git stash'),
    ]
]

keyboard.keymap = keymap

media_keys = MediaKeys()
keyboard.modules.append(media_keys)

encoder.pins = (board.D2, board.D3, board.D0)
encoder.set_action_on_up(KC.VOLU)
encoder.set_action_on_down(KC.VOLD)
encoder.set_action_on_press(KC.MUTE)

while True:
    keyboard.update()
    animate()
