import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digital import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.keys import KC
from kmk.handlers.stock import led_toggle
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

#unsure if these pins are correct however this can be easily fixed when i get the board (numbers gotten from pcb schematic)
keyboard.matrix = MatrixScanner(columns=[board.GP1,board.GP2,board.GP3], rows=[board.GP4,board.GP5])

encoderHandler = EncoderHandler()
keyboard.modules.append(encoderHandler)
encoderHandler.pins = ((board.GP9, board.GP8, board.GP10),)
encoderHandler.map = [(KC.VOLU, KC.VOLD, KC.MUTE)] #for the third option (KC.MUTE), im assuming this is for pressing the rotary encoder however this may change

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.END, KC.MPRV, KC.MNXT], #mapping keys based off of qmk's guide
    [KC.P7, KC.P8, KC.MPLY],
]

rgbHandler = RGB(pixel_pin=board.GP6, num_pixels=6)
rgbHandler.enabled = True
rgbHandler.brightness = 100 #tip from my friend to *not* set this to 256
keyboard.modules.append(rgbHandler)


if __name__ == '__main__':
    keyboard.go()