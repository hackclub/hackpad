import board
import busio
import analogio
import neopixel

from adafruit_mcp3426 import MCP3426
from adafruit_mcp23008 import MCP23008
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

import usb_hid

# Source: Adafruit
# TODO: Test with mac to find the correct report descriptor
# This is only one example of a gamepad report descriptor,
# and may not suit your needs.
GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x04,  #   Report ID (4)
    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x10,  #   Usage Maximum (Button 16)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x10,  #   Report Count (16)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x81,  #   Logical Minimum (-127)
    0x25, 0x7F,  #   Logical Maximum (127)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,        # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(6,),    # This gamepad sends 6 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable(
    (usb_hid.Device.CONSUMER_CONTROL,
     gamepad)
)

cc = ConsumerControl(usb_hid.devices)
gp1 = gamepad(usb_hid.devices)
gp2 = gamepad(usb_hid.devices)

i2c = busio.I2C(board.SCL, board.SDA)

adc = MCP3426(i2c)

mcp = MCP23008(i2c)

joystick_x_left = analogio.AnalogIn(board.GP26)
joystick_y_left = analogio.AnalogIn(board.GP27)
joystick_x_right = analogio.AnalogIn(board.GP28)
joystick_y_right = analogio.AnalogIn(board.GP29)

keyboard = KMKKeyboard()

for pin in range(8):
    mcp.setup(pin, MCP23008.IN)

keyboard.col_pins = [mcp.get_pin(i) for i in range(3)]
keyboard.row_pins = [mcp.get_pin(i + 3) for i in range(3)]

keyboard.keymap = [
    [
        [KC.MUTE, KC.VOLD, KC.VOLU],  # Media controls: Mute, Volume Down, Volume Up
        [KC.PLAY_PAUSE, KC.PREV_TRACK, KC.NEXT_TRACK],  # Media playback controls
        [KC.WEB_SEARCH, KC.NEW_TAB, KC.FIND],  # Web/Browser shortcuts
    ],
    [
        [KC.COPY, KC.PASTE, KC.CUT],  # Editing controls
        [KC.UNDO, KC.REDO, KC.SELECT_ALL],  # Editing shortcuts
        [KC.LCTRL, KC.LALT, KC.LSFT],  # Modifier keys
    ],
    [
        [KC.SCRN, KC.PRTSC, KC.CALC],  # Screenshot and other utilities
        [KC.LGUI, KC.RGUI, KC.SPC],  # GUI keys and space
        [KC.ESC, KC.TAB, KC.ENTER],  # Control keys
    ],
]

keyboard.diode_orientation = DiodeOrientation.COL2ROW

def read_joystick(joystick):
    return int((joystick.value / 65535) * 255) - 127

def update_joystick():
    # Read the joystick values (left and right)
    x_left = read_joystick(joystick_x_left)
    y_left = read_joystick(joystick_y_left)
    x_right = read_joystick(joystick_x_right)
    y_right = read_joystick(joystick_y_right)

    gp1.move_joysticks(
        x=x_left,
        y=y_left,
    )

    gp2.move_joysticks(
        x=x_right,
        y=y_right,
    )

old_volume = 0

def update_volume():
    slider_0_value = adc.read_voltage(channel=0)
    volume_level = int((slider_0_value / 65535) * 100)
    # TODO: make this better
    if volume_level > old_volume:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif volume_level < old_volume:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    old_volume = volume_level

old_brightness = 0

def update_brightness():
    slider_1_value = adc.read_voltage(channel=1)
    brightness_level = int((slider_1_value / 65535) * 100)
    if brightness_level > old_brightness:
        cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
    elif brightness_level < old_brightness:
        cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
    old_brightness = brightness_level

pixel = neopixel.NeoPixel(board.GP2, 9, brightness=0.5, auto_write=True)

def fade_colors():
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 255, 0),  # Yellow
        (0, 255, 255),  # Cyan
        (255, 0, 255),  # Magenta
        (255, 255, 255)  # White
    ]
    while True:
        for color in colors:
            for i in range(256):
                faded_color = tuple(int(c * i / 255) for c in color)
                pixel.fill(faded_color)
                time.sleep(0.01)

def update_inputs():
    update_joystick()
    update_volume()
    update_brightness()

if __name__ == '__main__':
    while True:
        update_inputs()
        keyboard.go()
        fade_colors()
