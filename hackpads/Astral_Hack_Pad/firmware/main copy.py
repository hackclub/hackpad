from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.display.oled import Oled, OledDisplayMode
from kmk.modules.usb_hid import USBHID
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
import board
import digitalio
import rotaryio
import displayio
import adafruit_displayio_ssd1306
import terminalio
from adafruit_display_text import label

# Initialize KMK
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(USBHID())
keyboard.extensions.append(MediaKeys())

# Define MX key pins based on the schematic
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)  # Columns
keyboard.row_pins = (board.GP5, board.GP9, board.GP10, board.GP11)  # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Rotary Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.GP8, board.GP9)
encoder_switch = digitalio.DigitalInOut(board.GP10)
encoder_switch.direction = digitalio.Direction.INPUT
encoder_switch.pull = digitalio.Pull.UP

# OLED Setup (128x64 display on I2C, connected to GP6 (SDA) & GP7 (SCL))
displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Define key layers with customizable function keys
LAYER_1 = [
    KC.F1, KC.F2, KC.F3,
    KC.F4, KC.F5, KC.F6,
    KC.F7, KC.F8, KC.F9,
    KC.F10, KC.F11, KC.F12,
]
LAYER_2 = [
    KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK,
    KC.VOLU, KC.VOLD, KC.MUTE,
    KC.BRIGHTNESS_UP, KC.BRIGHTNESS_DOWN, KC.SLEEP,
    KC.ESC, KC.ENTER, KC.SPACE,
]

# Track layer index
layer_index = 0

# Encoder handling function
def check_encoder():
    global layer_index
    last_position = encoder.position
    while True:
        if encoder.position > last_position:
            layer_index = (layer_index + 1) % 2  # Toggle layers
        elif encoder.position < last_position:
            layer_index = (layer_index - 1) % 2
        last_position = encoder.position
        keyboard.active_layers = [layer_index]
        update_oled()
        keyboard.go()

# OLED Update Function
def update_oled():
    splash = displayio.Group()
    text = f"Layer: {layer_index}"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=10, y=30)
    splash.append(text_area)
    display.show(splash)

# Assign layers to KMK
keyboard.keymap = [LAYER_1, LAYER_2]

# Run encoder checking in a loop
import supervisor
supervisor.set_next_stack_limit(4096)
import asyncio
async def main():
    while True:
        check_encoder()
        await asyncio.sleep(0.01)

import asyncio
asyncio.run(main())
