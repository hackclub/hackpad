# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.GP1, board.GP2, board.GP3, board.GP4]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

def open_youtube_playlist():
    return [
	KC.MACRO(os.system(f"start https://www.youtube.com/feed/playlists))  
    ]

def open_chat():
    return [
	KC.MACRO(os.system(https://mail.google.com/chat/u/0/#chat/home))  
    ]
def open_drive():
    return [
	KC.MACRO(os.system(f"start https://drive.google.com/drive/my-drive))  
    ]
def open_youtube():
    return [
	KC.MACRO(os.system(f"start https://www.youtube.com))  
    ]


# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MACRO(open_youtube), KC.MACRO(open_drive), KC.MACRO(open_chat), KC.MACRO(open_youtube_playlist)]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()