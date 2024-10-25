import time
from time import sleep
import _thread
import board
import kmk.kmk_keyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
# This is a seperate library for the sk6812.
# https://github.com/blaz-r/pi_pico_neopixel/tree/main?tab=readme-ov-file
from neopixel import Neopixel
#Rainbow setup
numpix = 8
strip = Neopixel(numpix, board.D0, 0, "RGBW")
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors_rgb = (red, orange, yellow, green, blue, indigo, violet)

# same colors as normaln rgb, just 0 added at the end
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))

# uncomment colors_rgb if you have RGB strip
# colors = colors_rgb
colors = colors_rgbw

strip.brightness(42)

# Define column and row pins for a 3x3 matrix
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
ROW1 = board.D3
ROW2 = board.D6
ROW3 = board.D7

# Create the keyboard instance
keyboard = KMKKeyboard()

# Define column and row pins
keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Define the keymap
keyboard.keymap = [
    [KC.1,  KC.2,  KC.3],  # Row 1
    [KC.4,  KC.RIGHT,  KC.LEFT],  # Row 2
    [KC.Y,  KC.N,  KC.NO],  # Row 3
]



def core0_thread():
    # Start the keyboard
    if __name__ == '__main__':
        keyboard.go()
        
core0_thread()

def core1_thread():
    #Rainbow Execute
    while True:
        for color in colors:
            for i in range(numpix):
                strip.set_pixel(i, color)
                time.sleep(0.01)
                strip.show()
            
second_thread = _thread.start_new_thread(core1_thread, ())


