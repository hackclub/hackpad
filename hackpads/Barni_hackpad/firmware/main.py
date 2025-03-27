import board
LED_CONNECTED = True
try:
    import neopixel
    led = neopixel.NeoPixel(board.D5, 1, auto_write=True)
except Exception as e:
    LED_CONNECTED = False

if LED_CONNECTED:
    led[0] = (0, 255, 0)
else:
    try:
        import digitalio
        led = digitalio.DigitalInOut(board.D5)
        led.direction = digitalio.Direction.OUTPUT
        led.value = True
    except Exception:
        pass

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Delay, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
PINS = [board.D3, board.D4, board.D2, board.D1]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

def run_app(file_path):
    return (
        Press(KC.LGUI),
        Tap(KC.R),
        Release(KC.LGUI),
        Delay(200),
        file_path,
        Tap(KC.ENTER),
    )

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
GITHUB_PATH = r"C:\Users\Barni\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
VSCODE_PATH = r"E:\Programs\Microsoft VS Code\Code.exe"
STEAM_PATH  = r"C:\Program Files (x86)\Steam\steam.exe"

OPEN_CHROME = KC.MACRO(*run_app(CHROME_PATH))
OPEN_GITHUB = KC.MACRO(*run_app(GITHUB_PATH))
OPEN_VSCODE = KC.MACRO(*run_app(VSCODE_PATH))
OPEN_STEAM  = KC.MACRO(*run_app(STEAM_PATH))

keyboard.keymap = [
    [OPEN_CHROME, OPEN_GITHUB, OPEN_VSCODE, OPEN_STEAM]
]

if __name__ == '__main__':
    keyboard.go()