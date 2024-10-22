# Cyao macropad firmware
# Rev 1.1
# Copyright 2024
# Licensed under zlib license
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.LED import LED, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306

COL0 = board.GP9;
COL1 = board.GP8;
COL2 = board.GP7;
COL3 = board.GP6;
ROW0 = board.GP3;
ROW1 = board.GP2;
ROW2 = board.GP1;
ROW3 = board.GP0;

LED_PIN = board.GP10;

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
        TextEntry(text='Cyao macropad!'   , x=0, y=0, x_anchor="M"),
        TextEntry(text='*Insert Saber Pic*', x=0, y=12, x_anchor="M"),
];

keyboard = KMKKeyboard();

macros = Macros();
keyboard.modules.append(macros);

keyboard.extensions.append(display);

led = LED(
    led_pin=[LED_PIN],
    animation_mode=AnimationModes.BREATHING,
    brightness=50
);
keyboard.extensions.append(led);

keyboard.col_pins = (COL0, COL1, COL2, COL3);
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3);
keyboard.diode_orientation = DiodeOrientation.COL2ROW;

SAVE = KC.MACRO(":w");
QUIT = KC.MACRO(":wq");

keyboard.keymap = [
    [SAVE,      KC.TAB,   KC.SCOLON, QUIT  ],
    [KC.R,      KC.I,     KC.A,      KC.G  ],
    [KC.H,      KC.J,     KC.K,      KC.L  ],
    [KC.LSHIFT, KC.LCTRL, KC.LALT,   KC.ESC],
];

if __name__ == '__main__':
    keyboard.go();

