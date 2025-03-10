import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Layer


keyboard = KMKKeyboard()


switch1 = digitalio.DigitalInOut(board.D7)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D0)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D3)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D4)
switch4.switch_to_input(pull=digitalio.Pull.UP)

switch5 = digitalio.DigitalInOut(board.D2)
switch5.switch_to_input(pull=digitalio.Pull.UP)

switch6 = digitalio.DigitalInOut(board.D1)
switch6.switch_to_input(pull=digitalio.Pull.UP)



keyboard.pins = {
    board.D3: KC.UP, 
    board.D4: KC.DOWN, 
    board.D1: KC.RIGHT,  
    board.D0: KC.LEFT,
    board.D2: KC.PGDN,    
    board.D7: KC.PGUP,    
}


if __name__ == "__main__":
    while True:
        keyboard.poll()