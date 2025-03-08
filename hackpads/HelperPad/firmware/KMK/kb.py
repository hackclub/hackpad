from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digital import DirectPin
from kmk.handlers.sequences import send_string
import board

keyboard = KMKKeyboard()

taste_pins = [
    board.GP10,  # SW1
    board.GP11,  # SW2
    board.GP12,  # SW3
    board.GP13,  # SW4
    board.GP14,  # SW5
    board.GP15,  # SW6
    board.GP16,  # SW7
    board.GP17,  # SW8
    board.GP18   # SW9
]

keyboard.matrix = DirectPin(taste_pins)

# SW1 | SW 4 | SW 7
# SW2 | SW 5 | SW 8
# SW3 | SW 6 | SW 9

action_1 = [KC.ESC] # SW1
action_2 = [KC.SPACE]   # SW2
action_3 = [KC.ENTER]   # SW3
action_4 = [send_string("Thank you HackClub")] # SW4
action_5 = [KC.F2]   # SW5
action_6 = [KC.F5]   # SW6
action_7 = [KC.F12]   # SW7
action_8 = [KC.F8, send_string("EXIT")] # SW8
action_9 = [send_string("Hello I am HelperPad")]  # SW9

keyboard.keymap = [
    action_1,  # SW1
    action_2,  # SW2
    action_3,  # SW3
    action_4,  # SW4
    action_5,  # SW5
    action_6,  # SW6
    action_7,  # SW7
    action_8,  # SW8
    action_9   # SW9
]

if __name__ == '__main__':
    keyboard.go()
