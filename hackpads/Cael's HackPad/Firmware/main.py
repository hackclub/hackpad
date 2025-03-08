import board
from kmk.modules.oled import SSD1306
from kmk.extensions import KMKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
import analogio

keyboard = KMKKeyboard()

# Matrix setup
keyboard.col_pins = [board.GPIO4, board.GPIO2, board.GPIO1]
keyboard.row_pins = [board.GPB5, board.GPB6, board.GPB7]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Slider setup
slider1 = analogio.AnalogIn(board.GPIO26)
slider2 = analogio.AnalogIn(board.GPIO27)

# OLED setup
oled1306 = SSD1306(
    i2c_addr=0x3C, i2c_device=board.I2C(scl=board.GPIO7, sda=board.GPIO6)
)


# gets the % position of the slider
def get_slider_percent(slider):
    return int((slider.value * 100) / 65535)


# puts the slider % on the screen
def oled_update(oled):
    oled.fill()
    oled.text(f"{get_slider_percent(slider1)}%", 0, 0)
    oled.text(f"{get_slider_percent(slider2)}%", 0, 10)
    oled.show()


keyboard.modules.append(oled1306)
keyboard.keymap = [[KC.Q, KC.W, KC.E, KC.A, KC.S, KC.D, KC.Z, KC.X, KC.C]]

# once I have it physically I'm going to have the sliders adjust mic & spotify volumes respectively, and the buttons will be either for a mini keyboard or mute/unmute/play/pause hotkeys
# for now, this will just ensure that the pin layouts are working as intended and the connections are correct
# the volume control will probably need a script running in the pc itself but that's ok!

if __name__ == "__main__":
    keyboard.go()
