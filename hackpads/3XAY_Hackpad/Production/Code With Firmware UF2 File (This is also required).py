import board #Allows for access to the board's systems
from digitalio import DigitalInOut, Direction, Pull #Allows for digital I/O access
import adafruit_pcf8547 #I/O expander library
from adafruit_debouncer import Button #Button presses
import usb_hid #USB Devices
from adafruit_hid.mouse import Mouse #Mouse clicks / wheel
from adafruit_hid.keyboard import Keyboard #Keyboard presses
from adafruit_hid.keycode import Keycode #Key press names
from adafruit_hid.consumer_control import ConsumerControl #Media presses
from adafruit_hid.consumer_control_code import ConsumerControlCode #Media press codes
import rotaryio #For encoder
import busio #For i2c access
import adafruit_ssd1306 #Display lib for ssd1306


i2c = board.I2C() #i2c object from the SDA/SCL pins

pcf = adafruit_pcf8547.PCF8574(i2c, 0x20) #Save the IO expander as an object with an address of 0x20 (all address pins to ground)

i2cPins = busio.I2C(board.SCL, board.SDA) #Get the I2C pins for OLED
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2cPins) #Creates an OLED object with a 128x32 resolution

#Get pins from PCF
p6 = pcf.get_pin(6) #Gets a DigitalInOut pin
p5 = pcf.get_pin(5)
p7 = pcf.get_pin(7)

#Get EC11 pins from PCF
p0 = pcf.get_pin(0)
p1 = pcf.get_pin(1)
p2 = pcf.get_pin(2)
p3 = pcf.get_pin(3)

#Get EC11 R1 pins and S1-3 pins from board
a3 = DigitalInOut(board.A3)
a2 = DigitalInOut(board.A2)
a8 = DigitalInOut(board.A8)
a9 = DigitalInOut(board.A9)
a10 = DigitalInOut(board.A10)

#Setup pins
a8.direction = Direction.INPUT
a8.pull = Pull.UP
a9.direction = Direction.INPUT
a9.pull = Pull.UP
a10.direction = Direction.INPUT
a10.pull = Pull.UP
p6.direction = Direction.INPUT
p6.pull = Pull.UP
p5.direction = Direction.INPUT
p5.pull = Pull.UP
p7.direction = Direction.INPUT
p7.pull = Pull.UP
a3.direction = Direction.INPUT
a2.direction = Direction.INPUT
p0.direction = Direction.INPUT
p1.direction = Direction.INPUT
p2.direction = Direction.INPUT
p3.direction = Direction.INPUT

#Create switches with their pin, a keypress duration of 175ms, a hold duration of 350ms, and outputs True when pressed
sw1 = Button(a8, 175, 350, True)
sw2 = Button(a9, 175, 350, True)
sw3 = Button(a10, 175, 350, True)
sw4 = Button(p6, 175, 350, True)
sw5 = Button(p5, 175, 350, True)
sw6 = Button(p7, 175, 350, True)

#Create encoders with their pins
e1 = rotaryio.IncrementalEncoder(a3, a2)
e2 = rotaryio.IncrementalEncoder(p0, p1)
e3 = rotaryio.IncrementalEncoder(p2, p3)

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

