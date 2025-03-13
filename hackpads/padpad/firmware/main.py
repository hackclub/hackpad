# You import all the IOs of your board
import board
import busio
import supervisor
import time

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Display setup
bus = busio.I2C(board.SCL, board.SDA);
driver = SSD1306(i2c=bus, device_address=0x3C);
display = Display(
    display=driver,
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.7
);

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(display);

# Define your pins here!
PINS = [board.D10, board.D9, board.D8, board.D7, board.D6, board.D3]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

# 1 : Lock screen (win + l)
# 2 : Mute on discord (ctrl + shift + m)
# 3 : Pause
# 4 : Screenshot (win + shift + s)
# 5 : Powertoys Color Picker (win + shift + c)
# 6 : Powertoys OCR (win + shift + t)

keyboard.keymap = [
    [KC.Macro(Press(KC.LWIN), Press(KC.L), Release(KC.L), Release(KC.LWIN)),
     KC.Macro(Press(KC.LCTRL), Press(KC.LSHIFT), Press(KC.M), Release(KC.M), Release(KC.LSHIFT), Release(KC.LCTRL)),
     KC.PAUSE, # not in kmk's doc but in qmk's : https://github.com/qmk/qmk_firmware/blob/master/docs/keycodes.md
     KC.Macro(Press(KC.LWIN), Press(KC.LSHIFT), Press(KC.S), Release(KC.S), Release(KC.LSHIFT), Release(KC.LWIN)),
     KC.Macro(Press(KC.LWIN), Press(KC.LSHIFT), Press(KC.C), Release(KC.C), Release(KC.LSHIFT), Release(KC.LWIN)),
     KC.Macro(Press(KC.LWIN), Press(KC.LSHIFT), Press(KC.T), Tap(KC.T), Release(KC.LSHIFT), Release(KC.LWIN))
     ],
]

current_media = {
    'title': '',
    'artist': '',
    'status': ''
}

def update_display():
    # Clear the display
    display.clear()
    
    # Add text entries for media info
    if current_media['title']:
        title = current_media['title'][:16]  # Truncate if too long
        artist = current_media['artist'][:16]
        status = current_media['status']
        
        display.entries = [
            TextEntry(0, 0, title, 1),
            TextEntry(0, 12, artist, 1),
            TextEntry(0, 24, status, 1)
        ]
    else:
        display.entries = [
            TextEntry(0, 12, "No media playing", 1)
        ]
    
    display.update()

def process_serial_data(): # Sent by the host's python script
    if supervisor.runtime.serial_bytes_available:
        data = input().strip()
        if data.startswith('MEDIA|'):
            parts = data.split('|')
            if len(parts) == 4:
                current_media['title'] = parts[1]
                current_media['artist'] = parts[2]
                current_media['status'] = parts[3]
                update_display()

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
    while True:
        process_serial_data()
        time.sleep(0.1)