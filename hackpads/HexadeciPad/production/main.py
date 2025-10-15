# All modules are in the firmware dir
import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence
import time

# Keyboard stuff
i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=100000)
mcp = MCP23017(i2c, address=0x20)
keyboard = KMKKeyboard()

# Add the media keys extension
keyboard.extensions.append(MediaKeys())

# Encoder state tracking for app switching
last_encoder_turn_time = 0
alt_held = False
encoder_handler = EncoderHandler()

def app_switch_encoder(encoder_state, delta):
    global last_encoder_turn_time, alt_held
    current_time = time.monotonic()
    
    if encoder_state.pressed:
        keyboard.tap_key(KC.LALT(KC.TAB))
        time.sleep(0.06)  # 60ms delay
        keyboard.release_key(KC.LALT, KC.TAB)
    else:
        if not alt_held:
            keyboard.press_key(KC.LALT, KC.TAB)
            time.sleep(0.06)
            keyboard.release_key(KC.TAB)
            alt_held = True
        
        if delta > 0:
            keyboard.tap_key(KC.RIGHT)  # Move right in app switcher
        elif delta < 0:
            keyboard.tap_key(KC.LEFT)  # Move left in app switcher
        
        last_encoder_turn_time = current_time

def check_alt_release():
    global last_encoder_turn_time, alt_held
    current_time = time.monotonic()
    if alt_held and (current_time - last_encoder_turn_time > 1):
        keyboard.release_key(KC.LALT)
        alt_held = False

encoder_handler.map = [
    (KC.VOLU, KC.VOLD, KC.MUTE),  # Encoder 1 - Volume Control
    app_switch_encoder  # Encoder 2 - App Switching
]

keyboard.modules.append(encoder_handler)

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# my pins
PINS = [board.D10, board.D9, board.D8, board.D7, board.D3, mcp.get_pin(0), mcp.get_pin(15), mcp.get_pin(14), mcp.get_pin(2), mcp.get_pin(1), mcp.get_pin(4), mcp.get_pin(3), mcp.get_pin(6), mcp.get_pin(5)]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

OPEN_VSCODE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("code"), KC.ENTER))
OPEN_GITHUB = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("github"), KC.ENTER))
OPEN_TERMIUS = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("termius"), KC.ENTER))
OPEN_KICAD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("kicad"), KC.ENTER))
OPEN_FUSION360 = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("fusion360"), KC.ENTER))
OPEN_STEAM = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("steam"), KC.ENTER))
OPEN_DISCORD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("discord"), KC.ENTER))
OPEN_NOTEPAD = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("notepad++"), KC.ENTER))
OPEN_VMWARE = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("vmware"), KC.ENTER))
OPEN_CHROME = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("chrome"), KC.ENTER))
OPEN_SPOTIFY = simple_key_sequence((KC.LGUI(KC.R), KC.MACRO_SLEEP_MS(100), KC.COPY("spotify"), KC.ENTER))

# silly keymap
keyboard.keymap = [
    [KC.MPRV, KC.MPLY, KC.MNXT, OPEN_VSCODE, OPEN_GITHUB, OPEN_TERMIUS, OPEN_KICAD, OPEN_FUSION360, OPEN_STEAM, OPEN_DISCORD, OPEN_NOTEPAD, OPEN_VMWARE, OPEN_CHROME, OPEN_SPOTIFY]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()