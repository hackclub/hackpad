import board
import digitalio
import displayio
import terminalio
import supervisor
from adafruit_display_text import label
from adafruit_displayio_ssd1306 import SSD1306_I2C
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
layers = Layers()
keyboard.modules.append(layers)

displayio.release_displays()
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
oled = SSD1306_I2C(128, 32, i2c)
splash = displayio.Group()
text_area = label.Label(terminalio.FONT, text="Mode: Writing", color=0xFFFFFF, x=10, y=10)
splash.append(text_area)
oled.show(splash)

LAYER_WRITING = 0
LAYER_PUBLISHING = 1
LAYER_PRODUCTIVITY = 2
LAYER_UTILITY = 3
current_layer = LAYER_WRITING

def update_oled():
    mode_text = ["Mode: Writing", "Mode: Publishing", "Mode: Productivity", "Mode: Utility"]
    text_area.text = mode_text[current_layer]

def switch_mode():
    global current_layer
    current_layer = (current_layer + 1) % 4
    update_oled()

def run_command(command):
    return [KC.LCTRL, KC.LALT, KC.T, KC.DELAY(100), *[KC(code) for code in command], KC.ENTER]

keyboard.keymap = [
    [
        KC.MO(1),
        run_command("code"),
        run_command("npm install"),
        run_command("npm run dev"),
        run_command("xdg-open ."),
        KC.NO,
        KC.NO
    ],

    [
        KC.MO(2),
        run_command("git add ."),
        run_command('git commit -m "update"'),
        run_command("git push"),
        run_command("vercel deploy"),
        run_command("heroku git:remote -a your-app-name"),
        KC.NO
    ],

    [
        KC.MO(3),
        KC.LCTRL(KC.C),
        KC.LCTRL(KC.V),
        run_command("brave-browser"),
        run_command("jetbrains-toolbox"),
        KC.NO,
        KC.NO
    ],

    [
        KC.MO(0),
        run_command("sudo apt update && sudo apt upgrade -y"),
        run_command("sudo systemctl restart NetworkManager"),
        run_command("htop"),
        run_command("sudo reboot"),
        run_command("sudo poweroff"),
        KC.NO
    ],
]

keyboard.keys_pressed.append(lambda: switch_mode())

if __name__ == '__main__':
    keyboard.go()
