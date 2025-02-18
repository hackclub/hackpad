import board, busio, displayio, terminalio, time, random

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

import digitalio

import adafruit_displayio_ssd1306
from adafruit_display_text import label

# Initialize keyboard
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.row_pins = (board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Enable layers
layers_ext = Layers()
keyboard.modules.append(layers_ext)

# Define OLED display
sda, scl = (board.D4, board.D5)
i2c = busio.I2C(scl, sda)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# Define Buzzer
buzzer = digitalio.DigitalInOut(board.D3)
buzzer.direction = digitalio.Direction.OUTPUT

def buzzer_on():
    buzzer.value = True

def buzzer_off():
    buzzer.value = False

def buzz():
    buzzer_on()
    time.sleep(0.1)
    buzzer_off()

# Stopwatch Variables
started_stopwatch = False
start_time = 0
stop_time = 0

# Keyboard shortcuts
save = simple_key_sequence((KC.LCTRL(KC.S),))
copy = simple_key_sequence((KC.LCTRL(KC.C),))
cut = simple_key_sequence((KC.LCTRL(KC.X),))
paste = simple_key_sequence((KC.LCTRL(KC.V),))
select_line = simple_key_sequence((KC.LSHIFT(KC.V),))

def update_oled(text):
    splash = displayio.Group()
    display.show(splash)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=10, y=30)
    splash.append(text_area)

# Stopwatch functionality
def start_stop_stopwatch():
    global started_stopwatch, start_time, stop_time
    if started_stopwatch:
        stop_time = time.monotonic()
        elapsed_time = stop_time - start_time
        update_oled(f"Time: {elapsed_time:.2f}s\n(Next to Restart)")
        started_stopwatch = False
    else:
        start_time = time.monotonic()
        update_oled("Stopwatch Running\n(Next to Stop)")
        started_stopwatch = True
    buzz()

# Rock, Paper, Scissors game logic
def play_rps(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    ai_choice = random.choice(choices)
    result = "Draw" if player_choice == ai_choice else (
        "You Win" if (player_choice == "Rock" and ai_choice == "Scissors") or
                      (player_choice == "Paper" and ai_choice == "Rock") or
                      (player_choice == "Scissors" and ai_choice == "Paper")
        else "You Lose"
    )
    update_oled(f"You: {player_choice}\nAI: {ai_choice}\n{result}")
    buzz()

# Reset game display
def reset_rps():
    update_oled("Rock Paper Scissors\nChoose an option")
    buzz()

class LayerSwitchKey(Key):
    def __init__(self, n):
        self.new_layer = n

    def on_press(self, keyboard):
        keyboard.layer = self.new_layer
        match self.new_layer:
            case 0:
                update_oled("MacroVerse!\nMode: Macropad (0)")
            case 1:
                update_oled("MacroVerse!\nMode: Stopwatch (1)\n(Next to start/stop)")
            case 2:
                update_oled("MacroVerse!\nMode: Rock Paper Scissors (2)\nChoose an option")
        buzz()
        return []

    def on_release(self, keyboard):
        return []

keyboard.keymap = [
    [  # Layer 0: Keyboard mode
        save, copy, cut,
        paste, select_line, LayerSwitchKey(1)
    ],
    [  # Layer 1: Stopwatch
        start_stop_stopwatch, KC.NO, KC.NO,
        KC.NO, KC.NO, LayerSwitchKey(2)
    ],
    [  # Layer 2: Rock Paper Scissors Game
        lambda: play_rps("Rock"), lambda: play_rps("Paper"), lambda: play_rps("Scissors"),
        reset_rps, KC.NO, LayerSwitchKey(0)
    ]
]

if __name__ == '__main__':
    keyboard.go()
