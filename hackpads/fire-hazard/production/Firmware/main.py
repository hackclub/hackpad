import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.pixelmap import PixelMap
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys
from kb import MacroPad
import time
from media_info import MediaInfo
from display_manager import DisplayManager
from led_manager import LEDManager

keyboard = MacroPad()

layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

encoder_handler.pins = ((board.A2, board.A3, board.A1),)
encoder_handler.map = [(
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ((KC.LEFT, KC.RIGHT, KC.ENTER),),
)]

rgb = RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=4,
    num_strands=1,
)
keyboard.extensions.append(rgb)

led_manager = LEDManager(rgb.pixels)

displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

media = MediaInfo()
splash = displayio.Group()

album_group = displayio.Group(x=2, y=16)
album_bitmap = media.get_album_art()
album_palette = displayio.Palette(1)
album_palette[0] = 0xFFFFFF
album_tile = displayio.TileGrid(album_bitmap, pixel_shader=album_palette)
album_group.append(album_tile)
splash.append(album_group)

text_area = label.Label(
    terminalio.FONT,
    text="Waiting...",
    color=0xFFFFFF,
    x=36,
    y=24,
    scale=1
)
splash.append(text_area)
display.show(splash)

display_manager = DisplayManager(display, splash, media)

def update_display():
    track_info = media.get_media_info()
    text_area.text = track_info
    album_bitmap = media.get_album_art()
    album_tile.bitmap = album_bitmap

keyboard.keymap = [
    [
        KC.MT(KC.M, KC.LCTL(KC.LSFT)),
        KC.MT(KC.D, KC.LCTL(KC.LSFT)),
        KC.LGUI(KC.D),
        KC.LCTL(KC.LSFT(KC.M)) + KC.LCTL(KC.LSFT(KC.D)) + KC.LGUI(KC.D),
    ],
    [KC.LSFT, KC.LCTL, KC.LALT, KC.MO(1)]
]

def handle_key_event(key_event):
    if key_event.pressed:
        if key_event.key_number == 0:
            led_manager.toggle_mute()
        elif key_event.key_number == 1:
            led_manager.toggle_deafen()

if __name__ == "__main__":
    last_update = 0
    while True:
        keyboard.go()
        current_time = time.monotonic()
        
        key_event = keyboard.events.get()
        if key_event:
            display_manager.register_activity()
            handle_key_event(key_event)
        
        if current_time - last_update >= 5:
            update_display()
            last_update = current_time

        display_manager.update()
        led_manager.update_chain()
