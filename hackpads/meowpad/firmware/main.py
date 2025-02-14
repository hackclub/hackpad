import board
import digitalio
import rotaryio
import analogio
import busio
import displayio
import terminalio
import usb_cdc
import time
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from kmk.kmk_keyboard import KMKKEYBOARD
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC

keyboard = KMKKEYBOARD()

displayio.release_displays()
i2c = busio.I2C(board.GP7, board.GP6)
displaybus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(displaybus, width=128, height=32)

def showtext(text):
    displaygrp = displayio.Group()
    textarea = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=5, y=10)
    displaygrp.append(textarea)
    display.show(displaygrp)

def updatesysresources(cpu, ram):
    displaygrp = displayio.Group()
    textarea = label.Label(terminalio.FONT, text=f"CPU: {cpu}% RAM: {ram}%", color=0xFFFFFF, x=5, y=10)
    displaygrp.append(textarea)
    display.show(displaygrp)

serial = usb_cdc.data

def readserial():
    if serial.in_waiting > 0:
        try:
            line = serial.readline().decode("utf-8").strip()
            cpu, ram = map(int, line.split(","))
            updatesysresources(cpu, ram)
        except Exception as e:
            showtext("serial error")

# keymaps
keyboard.keymap = [
#   [q, w, e, a, s, d]
#   [SW2, SW1, ROT, SW3, SW4, SW6]
    [KC.Q, KC.W, KC.LSHIFT, KC.A, KC.S, KC.D],
    [KC.LSHIFT, KC.UP, KC.ESC, KC.LEFT, KC.DOWN, KC.RIGHT],
    [KC.COLN, KC.J, KC.ESC, KC.H, KC.K, KC.L]
]

# currentlayer = 0

# oled
# oled = Oled(
#     OledData(
#         corner_one="",
#         corner_two="mode: wasd",
#         corner_three="",
#         corner_four=""
#     ),
#     toDisplay=OledDisplayMode.TXT,
#     flip=False
# )

# keyboard.extensions.append(oled)

# def updateoled():
#     if currentlayer == 0:
#         oled.data.corner_two = "mode: wasd"
#     elif currentlayer == 1:
#         oled.data.corner_two = "mode: arrows"
#     elif currentlayer == 2:
#         oled.data.corner_two = "mode: vim"
#     oled.data.corner_one = ""
#     time.sleep(5)
#     oled.data.corner_two = ""

# def changelayer(newlayer):
#     global currentlayer
#     currentlayer = newlayer
#     keyboard.active_layers = [currentlayer]
#     update_oled()

# key matrix
keyboard.matrix = MatrixScanner(
    cols=[board.GP27, board.GP28, board.GP29],
    rows=[board.GP02, board.GP01],
    diod_orientation=DiodeOrientation.COL2ROW
)

# rotary encoder
encoder = rotaryio.IncrementalEncoder(board.GP03, board.GP04)
encoderswitch = digitalio.DigitalInOut(board.GP12)
encoderswitch.direction = digitalio.Direction.INPUT
encoderswitch.pull = digitalio.Pull.UP

# slider
slider = analogio.AnalogIn(board.GP26)

def getsliderval():
    return slider.value // 257

def adjustvol():
    volumelevel = getsliderval()
    keyboard.tap_key(KC.VOLU, volume_level // 25)

def rotaryhandler():
    position = encoder.position
    if position > 0:
        keyboard.active_layers = [min(len(keyboard.keymap)-1, keyboard.active_layers[0]+1)]
    elif position < 0:
        keyboard.active_layers = [max(0, keyboard.active_layers[0]-1)]

keyboard.before_matrix_scan.append(adjustvol)
keyboard.before_matrix_scan.append(rotaryhandler)
keyboard.before_matrix_scan.append(readserial)

if __name__ == "__main__":
    showtext("waiting for data...")
    keyboard.go()
