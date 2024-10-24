import board #Allows for access to the board's systems
from inputs import Switch, Enc
from adafruit_debouncer import Button #Button presses
import usb_hid #USB Devices
from adafruit_hid.mouse import Mouse #Mouse clicks / wheel
from adafruit_hid.keyboard import Keyboard #Keyboard presses
from adafruit_hid.keycode import Keycode #Key press names
from adafruit_hid.consumer_control import ConsumerControl #Media presses
from adafruit_hid.consumer_control_code import ConsumerControlCode #Media press codes
import busio #For i2c access
import adafruit_ssd1306 #Display lib for ssd1306


i2cPins = busio.I2C(board.SCL, board.SDA) #Get the I2C pins for OLED
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2cPins) #Creates an OLED object with a 128x32 resolution

#Create switch objects
sw1 = Switch(0, boardPin=board.A8)
sw2 = Switch(0, boardPin=board.A9)
sw3 = Switch(0, boardPin=board.A10)
sw4 = Switch(5, pcf=True)
sw5 = Switch(6, pcf=True)
sw6 = Switch(7, pcf=True)

#Create switches with their pin, a keypress duration of 175ms, a hold duration of 350ms, and outputs True when pressed
sw1 = sw1.setup(175, 350)
sw2 = sw2.setup(175, 350)
sw3 = sw3.setup(175, 350)
sw4 = sw4.setup(175, 350)
sw5 = sw5.setup(175, 350)
sw6 = sw6.setup(175, 350)

#Create encoders with their pins
e1 = Enc(boardPin1=board.A3, boardPin2=board.A2)
e1 = e1.setup()
e2 = Enc(pcfPin1=0, pcfPin2=1)
e2 = e2.setup()
e3 = Enc(pcfPin1=2, pcfPin2=3)
e3 = e3.setup()

#Create last_pos objects
last_pos1 = 0
last_pos2 = 0
last_pos3 = 0

#Create mouse object
mouse = Mouse(usb_hid.devices)

#Create keyboard object
kbd = Keyboard(usb_hid.devices)

#Create media object
media = ConsumerControl(usb_hid.devices)

while True: #Main loop
    #Update switch state
    sw1.update()
    sw2.update()
    sw3.update()
    sw4.update()
    sw5.update()
    sw6.update()

    #OLED refresh
    oled.fill(0) #Clear screen
    oled.text("Test text", 0, 0) #Writes "test text" at (0,0)
    oled.text("Switch 6 state: " + sw6.pressed, 0, 20) #Shows the state of SW6 at (0,20)
    oled.show() #Update the display

    #Switch outputs
    if sw1.pressed:
        kbd.send(Keycode.SPACEBAR) #Play/pause

    if sw2.pressed:
        kbd.send(Keycode.F) #Fullscreen in Davinci

    if sw3.pressed:
        kbd.send(Keycode.CTRL, Keycode.S) #Save

    if sw4.pressed:
        kbd.send(Keycode.M) #Marker in Davinci

    if sw5.pressed:
        kbd.send(Keycode.CTRL, Keycode.BACKSLASH) #Split clip in Davinci

    if sw6.pressed:
        kbd.send(Keycode.ALT, Keycode.BACKSLASH) #Join clip in Davinci

    #Encoder stuff
    pos1 = e1.position
    pos2 = e2.position
    pos3 = e3.position

    if last_pos1 != pos1:
        if last_pos1 > pos1:
            media.send(ConsumerControlCode.VOLUME_DECREMENT) #Counter-clockwise
        else:
            media.send(ConsumerControlCode.VOLUME_INCREMENT) #Clockwise

    if last_pos2 != pos2:
        if last_pos1 > pos1:
            media.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK) #Placeholder, supposed to be horizontal scroll
        else:
            media.send(ConsumerControlCode.SCAN_NEXT_TRACK)

    if last_pos3 != pos3:
        if last_pos1 > pos1:
            kbd.send(Keycode.CTRL, Keycode.EQUALS)
        else:
            kbd.send(Keycode.CTRL, Keycode.MINUS)

    #Reset last position var
    last_pos1 = pos1
    last_pos2 = pos2
    last_pos3 = pos3

