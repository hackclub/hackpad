// looked at CyaoPad and docs

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

COL0 = board.GP0;
COL1 = board.GP1;
COL2 = board.GP2;
ROW0 = board.GP26;
ROW1 = board.GP27;
ROW2 = board.GP28;

bus = busio.I2C(board.GP_SCL, board.GP_SDA);
driver = SSD1306(i2c=bus, device_address=0x3C);

display = Display(
    display=driver,
    width=128,
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
);

display.entries = [
        TextEntry(text='pizzaPad :)', x=0, y=0, x_anchor="M"),
];

keyboard = KMKKeyboard();

macros = Macros();
keyboard.modules.append(macros);
keyboard.extensions.append(display);

keyboard.col_pins = (COL0, COL1, COL2);
keyboard.row_pins = (ROW0, ROW1, ROW2);
keyboard.diode_orientation = DiodeOrientation.COL2ROW;

keyboard.keymap = [
    [KC.KP_1,   KC.KP_2,  KC.KP_3,],
    [KC.KP_4,   KC.KP_5,  KC.KP_6,],
    [KC.KP_7,   KC.KP_8,  KC.KP_9,],
];

if __name__ == '__main__':
    keyboard.go();
