import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence


# 4x4 keyboard
keyboard = KMKKeyboard()

# Define matrix pins based on the schematic, using GP pins
keyboard.col_pins = (
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
)  # COLUMN_0, COLUMN_1, COLUMN_2, COLUMN_3
keyboard.row_pins = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
)  # ROW_0, ROW_1, ROW_2, ROW_3
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Custom key sequences (as before)
OPEN_GITHUB = simple_key_sequence(
    (KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("https://github.com"), KC.ENTER)
)

OPEN_DISCORD = simple_key_sequence(
    (KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("discord"), KC.ENTER)
)
# OPEN_MSWORD = simple_key_sequence(
#   (KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("winword"), KC.ENTER)
# )
# Requires adding qFLIPPER to System Path variable
OPEN_QFLIPPER = simple_key_sequence(
    (KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("qFlipper.exe"), KC.ENTER)
)

SHUTDOWN = simple_key_sequence((KC.LGUI(KC.X), KC.U, KC.U))  # Windows shutdown sequence

# Define keymap

# Should look like this
# 0     1       2       BACKSPACE (DONE)
# Q     W       E       SPACE
# A     S       D       ENTER
# GITHUB DISCORD   LEFTALT SHUTDOWN
keyboard.keymap = [
    [
        [KC.N0, KC.N1, KC.N2, KC.BACKSPACE],
        [KC.Q, KC.W, KC.E, KC.SPACE],
        [KC.A, KC.S, KC.D, KC.ENTER],
        [OPEN_GITHUB, OPEN_DISCORD, OPEN_QFLIPPER, SHUTDOWN],
    ]
]

if __name__ == "__main__":
    keyboard.go()
