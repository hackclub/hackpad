import board
import digitalio
import adafruit_matrixkeypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

rows = [board.D2, board.D3, board.D4]
cols = [board.D5, board.D6, board.D7]

keys = [
    [1, 2, 3],
    [4, 5, 6],
    [None, 7, None]
]

row_pins = [digitalio.DigitalInOut(pin) for pin in rows]
col_pins = [digitalio.DigitalInOut(pin) for pin in cols]
keypad = adafruit_matrixkeypad.Matrix_Keypad(row_pins, col_pins, keys)

keyboard = Keyboard(usb_hid.devices)

key_mappings = {
    1: Keycode.A,
    2: Keycode.B,
    3: Keycode.C,
    4: Keycode.D,
    5: Keycode.E,
    6: Keycode.F,
    7: Keycode.G
}

while True:
    keys_pressed = keypad.pressed_keys
    for key in keys_pressed:
        if key in key_mappings:
            keyboard.press(key_mappings[key])
    if not keys_pressed:
        keyboard.release_all()
