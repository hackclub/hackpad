# Basic, probably not working firmware
import board
import busio
import time
import board
from rainbowio import colorwheel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
COL0 = board.D0;
COL1 = board.D1;
COL2 = board.D2; 
ROW0 = board.D0;
ROW1 = board.D6;
ROW2 = board.D7;
LED_PIN = board.D9;

bus = busio.I2C(board.SCL, board.SDA);

driver = SSD1306(i2c=bus, device_address=0x3C);

display = Display(
    display=driver,
    width=128,
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.7
);

keyboard = KMKKeyboard();

macros = Macros();
keyboard.modules.append(macros);
keyboard.extensions.append(display);

keyboard.col_pins = (COL0, COL1, COL2, COL3);
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3);
keyboard.diode_orientation = DiodeOrientation.COL2ROW;

rgb = RGB(pixel_pin=board.D10, num_pixels=9, animation_speed=1, animation_mode=AnimationModes.SWIRL)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [A, B, C,
     E, F, G,
     I, J, K],
];

if __name__ == '__main__':
    keyboard.go();
