from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.split import SplitKeyboard
from kmk.extensions.led import RGB
import board
import busio
from kmk.modules.mcp23017 import MCP23017
import digitalio
import neopixel
import time
import math

keyboard = KMKKeyboard()

# GPIO Setup for the Key Matrix
keyboard.matrix = MatrixScanner(
    cols=[board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7,
          board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16],
    rows=[board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22],
    diodes='COL2ROW',  # Updated to include diodes
)

# I2C Setup for MCP23017
i2c = busio.I2C(board.GP27, board.GP26)
io_expander = MCP23017(i2c)

# Setup for Rotary Encoders via MCP23017
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = [
    ((io_expander.gpb2, io_expander.gpb3), io_expander.gpb0),  # Encoder 1
    ((io_expander.gpb4, io_expander.gpb5), io_expander.gpb1),  # Encoder 2
]

# Define encoder actions
encoder_handler.map = [
    # Encoder 1: Rotate to skip songs, click to mute mic
    [KC_MEDIA_NEXT_TRACK, KC_MEDIA_PREV_TRACK, KC_AUDIO_MUTE],
    # Encoder 2: Rotate to control volume, click to mute audio
    [KC_AUDIO_VOL_UP, KC_AUDIO_VOL_DOWN, KC_MEDIA_PLAY_PAUSE],
]

# RGB LED Setup (SK6812 on GPIO0)
pixels = neopixel.NeoPixel(board.GP0, 8, brightness=0.5, auto_write=False)

def wave_effect():
    t = time.monotonic()
    for i in range(8):
        hue = (math.sin(t + i * 0.5) + 1) / 2  # Generate a wave effect
        pixels[i] = (int(255 * hue), int(255 * (1 - hue)), 128)
    pixels.show()

# Basic Keymap
keyboard.keymap = [
    ["KC_ESC", "KC_1", "KC_2", "KC_3", "KC_4", "KC_5", "KC_6", "KC_7", "KC_8", "KC_9", "KC_0", "KC_MINUS", "KC_EQUAL", "KC_BSPACE", "KC_HOME", "KC_PGUP",
     "KC_TAB", "KC_Q", "KC_W", "KC_E", "KC_R", "KC_T", "KC_Y", "KC_U", "KC_I", "KC_O", "KC_P", "KC_LBRACKET", "KC_RBRACKET", "KC_BSLASH", "KC_END", "KC_PGDOWN",
     "KC_CAPS", "KC_A", "KC_S", "KC_D", "KC_F", "KC_G", "KC_H", "KC_J", "KC_K", "KC_L", "KC_SCOLON", "KC_QUOTE", "KC_ENTER", "KC_UP", "KC_DEL", "KC_INSERT",
     "KC_LSHIFT", "KC_Z", "KC_X", "KC_C", "KC_V", "KC_B", "KC_N", "KC_M", "KC_COMMA", "KC_DOT", "KC_SLASH", "KC_RSHIFT", "KC_LEFT", "KC_DOWN", "KC_RIGHT", "KC_FN",
     "KC_LCTRL", "KC_LGUI", "KC_LALT", "KC_SPACE", "KC_RALT", "KC_RCTRL"]
]

if __name__ == '__main__':
    while True:
        wave_effect()
        keyboard.go()