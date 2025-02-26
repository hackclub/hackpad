# DEAD CODE, NOT DONE!

print("Hackpad Testing!")

# Basic imports for orpheuspad
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.extensions.RGB import RGB
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

# Extra features

print(dir(board))

i2c = busio.I2C(board.GP_SCL, board.GP_SDA)
mcp = MCP23017(i2c)

keyboard = KMKKeyboard()

# RGB imports
# TODO: ADD PINS
rgb = RGB(pixel_pin=board.GP7, num_pixels=12)
keyboard.extensions.append(rgb)

# TODO: add waveshare display

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # regular direction encoder and a button
    (
        board.GP2,
        board.GP1,
        board.GP3,
    ),  # encoder #1 
)

encoder_handler.map = [
    ((KC.UP, KC.DOWN), ),
]

keyboard.keymap = [[
    KC.AUDIO_VOL_DOWN,
    KC.AUDIO_VOL_UP,
]]

if __name__ == '__main__':
    keyboard.go()
