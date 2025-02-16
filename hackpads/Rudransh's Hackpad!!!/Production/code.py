import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.extensions.media_keys import MediaKeys
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D5, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Custom key definitions
LOCK_PC = simple_key_sequence((KC.LGUI(KC.L),))
SNIPPING_TOOL = simple_key_sequence((KC.LGUI, KC.LSHIFT, KC.S))
OPEN_DISCORD = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'C:\\Users\\YourUsername\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe', KC.ENTER))
OPEN_WEBSITE = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'https://yourwebsite.com', KC.ENTER))
OPEN_ROBLOX = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'C:\\Program Files (x86)\\Roblox\\Versions\\version-{hash}\\RobloxPlayerBeta.exe', KC.ENTER))
OPEN_EDGE = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'msedge', KC.ENTER))
OPEN_GITHUB = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'https://github.com', KC.ENTER))
NEW_GITHUB_REPO = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'https://github.com/new', KC.ENTER))
PYTHON_PRINT = simple_key_sequence((
    'for i in range(100):\n    print("Your word here")\n',
))
OPEN_TERMINAL = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'cmd', KC.ENTER))
OPEN_VSCODE = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'code', KC.ENTER))
OPEN_PW_WEBSITE = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'https://yourpwwebsite.com', KC.ENTER))
GITHUB_COMMIT = simple_key_sequence((KC.LCTRL(KC.K), KC.LCTRL(KC.ENTER)))
OPEN_SLACK = simple_key_sequence((KC.LGUI(KC.R), KC.ENTER, 'slack:', KC.ENTER))

keyboard.keymap = [
    [
        LOCK_PC,     KC.MUTE,    SNIPPING_TOOL, OPEN_DISCORD,   OPEN_WEBSITE,
        OPEN_ROBLOX, OPEN_EDGE,  OPEN_GITHUB,   NEW_GITHUB_REPO, PYTHON_PRINT,
        OPEN_TERMINAL, OPEN_VSCODE, OPEN_PW_WEBSITE, GITHUB_COMMIT, OPEN_SLACK
    ]
]

if __name__ == '__main__':
    keyboard.go()