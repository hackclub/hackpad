import board
import busio
import displayio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.keys import simple_key_sequence
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry

# define the kb
keyboard = KMKKeyboard()

# matrix pins based on schhematic
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D9, board.D10, board.D6)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# custom key definitions

#       APP KEYS
OPEN_DISCORD = simple_key_sequence(KC.LGUI(KC.SPACE), "discord", KC.ENTER )
OPEN_TERMINAL = simple_key_sequence(KC.LGUI(KC.SPACE), "terminal", KC.ENTER )
OPEN_VSCODE = simple_key_sequence(KC.LGUI(KC.SPACE), "vscode", KC.ENTER )
OPEN_CHROME = simple_key_sequence(KC.LGUI(KC.SPACE), "chrome", KC.ENTER )
OPEN_SLACK = simple_key_sequence(KC.LGUI(KC.SPACE), "slack", KC.ENTER )
OPEN_CHATGPT = simple_key_sequence(KC.LGUI(KC.SPACE), "chatgpt", KC.ENTER )
OPEN_NOTION = simple_key_sequence(KC.LGUI(KC.SPACE), "notion", KC.ENTER )
OPEN_SPOTIFY = simple_key_sequence(KC.LGUI(KC.SPACE), "spotify", KC.ENTER )
OPEN_MESSAGES = simple_key_sequence(KC.LGUI(KC.SPACE), "messages", KC.ENTER )
OPEN_WHATSAPP = simple_key_sequence(KC.LGUI(KC.SPACE), "whatsapp", KC.ENTER )
OPEN_FINDER = simple_key_sequence(KC.LGUI(KC.SPACE), "finder", KC.ENTER )

#  define keymap
keyboard.keymap = [
    [OPEN_DISCORD, OPEN_TERMINAL, OPEN_VSCODE, KC.NO],
    [OPEN_CHROME, OPEN_SLACK, OPEN_CHATGPT, OPEN_NOTION],
    [OPEN_SPOTIFY, OPEN_MESSAGES, OPEN_WHATSAPP, OPEN_FINDER]
]

if __name__ == '__main__':
    keyboard.go()
