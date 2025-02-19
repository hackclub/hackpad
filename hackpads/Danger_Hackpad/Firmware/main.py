import board
import supervisor
import usb_hid

# Imports from the KMK library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.handlers.system import SystemExec

# Initialize the keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define button pins
PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6, board.D7]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


CMD_CHROME = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile {num}"'
CMD_SPOTIFY = r'start spotify'
CMD_VSCODE = r'start code'
CMD_CHATGPT = r'start https://chat.openai.com'


keyboard.keymap = [
    [
        SystemExec(CMD_CHROME.format(num=0)),  # Chrome Profile 1
        SystemExec(CMD_CHROME.format(num=1)),  # Chrome Profile 2
        SystemExec(CMD_CHROME.format(num=2)),  # Chrome Profile 3
        SystemExec(CMD_CHROME.format(num=3)),  # Chrome Profile 4
        SystemExec(CMD_CHATGPT),               # Open ChatGPT
        SystemExec(CMD_SPOTIFY),               # Open Spotify
        SystemExec(CMD_VSCODE),                # Open VS Code
    ]
]


if __name__ == '__main__':
    keyboard.go()
