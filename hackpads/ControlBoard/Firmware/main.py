import board
import busio
import keypad
import usb_hid
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.led import RGB
from kmk.extensions.display import Oled
from kmk.hid import HIDConsumerControl, HIDUsage
from adafruit_mcp230xx.mcp23017 import MCP23017

keyboard = KMKKeyboard()

i2c = busio.I2C(board.GP6, board.GP7)
mcp = MCP23017(i2c)

keyboard.matrix = keypad.KeyMatrix(
    row_pins=[board.GP4, board.GP2, board.GP1],
    column_pins=[board.GP26, board.GP27, board.GP28],
    columns_to_anodes=False,
)
rgb = RGB(
    pixel_pin=mcp.get_pin(6),
    num_pixels=16,
    val_limit=100,
    hue_default=0,
    animation='RIPPLE',
)
keyboard.extensions.append(rgb)

# OLED Setup
oled = Oled(
    width=128, height=32, i2c=busio.I2C(board.GP6, board.GP7)
)

def oled_callback(oled):
    oled.clear()
    oled.text(f'Batt: {battery}%', 0, 0)
    oled.text(f'Vol: {volume}%', 0, 10)
    oled.show()

oled.set_callback(oled_callback)
keyboard.extensions.append(oled)

# Host Communication
import usb_cdc
serial = usb_cdc.data

def handle_host_commands():
    if serial.in_waiting > 0:
        data = serial.readline().decode().strip()
        if data.startswith("BATT:"):
            global battery
            battery = int(data.split(":")[1])
        elif data.startswith("VOL:"):
            global volume
            volume = int(data.split(":")[1])

if __name__ == '__main__':
    while True:
        handle_host_commands()
        keyboard.go()