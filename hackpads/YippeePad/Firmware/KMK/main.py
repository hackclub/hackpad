import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.mcp23017 import MCP23017
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledData
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

# Add I2C MCP23017 Expander
mcp23017 = MCP23017(address=0x20)
keyboard.modules.append(mcp23017)

# Add Rotary Encoders
encoder_handler = EncoderHandler()
encoder_handler.pins = [(board.GP6, board.GP7), (board.GP8, board.GP9)]
keyboard.modules.append(encoder_handler)

# Define Websites (Modify URLs as needed)
website_shortcuts = [
    send_string("https://gmail.com\n"),
    send_string("https://youtube.com\n"),
    send_string("https://github.com\n"),
    send_string("https://reddit.com\n"),
    send_string("https://twitter.com\n"),
    send_string("https://discord.com\n"),
    send_string("https://twitch.tv\n"),
    send_string("https://spotify.com\n"),
    send_string("https://stackoverflow.com\n"),
    send_string("https://chatgpt.com\n"),
    send_string("https://amazon.com\n"),
    send_string("https://netflix.com\n"),
]

# Define Keymap for Switches
keyboard.keymap = [website_shortcuts]

# Rotary Encoders Functionality
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD)),  # Encoder 1: Volume up/down
    ((KC.BRIU, KC.BRID)),  # Encoder 2: Brightness up/down
]

# OLED Display (GIF Support)
oled = Oled(
    OledData(
        gif="user_gif.gif",  # Replace with the actual GIF file you upload
        mode=OledDisplayMode.GIF,
    ),
    flip=True
)
keyboard.extensions.append(oled)

# Start Keyboard
if __name__ == '__main__':
    keyboard.go()