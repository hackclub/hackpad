from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oled import Oled, OledDisplayMode
from time import monotonic
import board
import busio
import rtc
from adafruit_pcf8574 import PCF8574
import subprocess

i2c = busio.I2C(board.SCL, board.SDA)

# PCF8574AN setup
pcf8574 = PCF8574(i2c, 0x20)

# Define the GPIO pins for rotary encoders
encoder_pins_1 = (pcf8574.get_pin(0), pcf8574.get_pin(1))  # Encoder 1 (Volume)
encoder_pins_2 = (pcf8574.get_pin(3), pcf8574.get_pin(4))  # Encoder 2 (Brightness)

keyboard = KMKKeyboard()


keyboard.matrix = MatrixScanner(
    row_pins=(board.D3, board.D6, board.D7, board.D8),  # Rows
    col_pins=(board.D0, board.D1, board.D2),  # Columns
    diodes=MatrixScanner.DIODE_COL2ROW  # Diode direction
)

# Enable encoder handling
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Configure the encoders
encoder_handler.pins = [
    (encoder_pins_1, pcf8574.get_pin(2)),  # First encoder (Volume) and switch
    (encoder_pins_2, pcf8574.get_pin(5)),  # Second encoder (Brightness) and switch
]

# Set up OLED
oled_ext = Oled(
    i2c=i2c,
    width=128,
    height=32,
    display_mode=OledDisplayMode.LAYER
)
keyboard.extensions.append(oled_ext)

# Add media key support (for volume control)
keyboard.extensions.append(MediaKeys())

# Variables for Pomodoro timer
pomodoro_start_time = 0
pomodoro_in_progress = False
pomodoro_duration = 25 * 60  # 25 minutes (in seconds)

# Define the keymap with macros
keyboard.keymap = [
    [KC.FX, KC.SLACK, KC.VS, KC.ESC,   # Row 0: open apps (Firefox, Slack, VSCode)
     KC.COMMIT, KC.LOCK, KC.PUSH, KC.SYNC,   # Row 1: Git macros (commit, lock, push, sync)
     KC.A, KC.B, KC.C, KC.D],  # Row 2: Regular keys
]

# Function to open an app based on key
def open_app(app):
    try:
        subprocess.run(app, check=True)
    except Exception as e:
        print(f"Failed to open {app}: {e}")

# Rotary encoder behavior
@encoder_handler.handler
def on_encoder_update(index, clockwise):
    global pomodoro_start_time, pomodoro_in_progress
    
    if index == 0:  # First encoder (Volume)
        if clockwise:
            keyboard.send(KC.VOLU)  # Volume up
        else:
            keyboard.send(KC.VOLD)  # Volume down
    elif index == 1:  # Second encoder (Brightness)
        if clockwise:
            oled_ext.set_brightness(min(oled_ext.brightness + 0.1, 1.0))  # Increase brightness
        else:
            oled_ext.set_brightness(max(oled_ext.brightness - 0.1, 0.0))  # Decrease brightness

# Encoder press behavior (Pomodoro timer toggle)
@encoder_handler.handler
def on_encoder_click(index):
    global pomodoro_start_time, pomodoro_in_progress

    if index == 0:  # First encoder (Volume)
        # When clicked, start or stop the Pomodoro timer
        if not pomodoro_in_progress:
            pomodoro_start_time = monotonic()
            pomodoro_in_progress = True
        else:
            pomodoro_in_progress = False
            pomodoro_start_time = 0
    elif index == 1:  # Second encoder (Brightness)
        # Reset the Pomodoro timer
        pomodoro_in_progress = False
        pomodoro_start_time = 0

# Update OLED with time and Pomodoro timer
def update_oled():
    import time
    now = time.localtime()
    
    if pomodoro_in_progress:
        elapsed = monotonic() - pomodoro_start_time
        time_remaining = pomodoro_duration - elapsed
        minutes, seconds = divmod(int(time_remaining), 60)
        oled_ext.display_text(f"Pomodoro: {minutes:02d}:{seconds:02d}", 0, 0)
    else:
        oled_ext.display_text(f"Time: {now.tm_hour:02d}:{now.tm_min:02d}", 0, 0)

# Execute the update every second
keyboard.timed_functions.append(update_oled)

# Run the keyboard
if __name__ == '__main__':
    keyboard.go()
