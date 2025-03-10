import board #Allows for access to the board's systems
from digitalio import DigitalInOut, Direction, Pull #Allows for digital I/O access
import adafruit_pcf8547 #I/O expander library
from adafruit_debouncer import Button #Button presses

class Switch:
    def __init__ (self, pin, pcf=False, boardPin=None):
        self.pin = pin
        self.pcf = pcf
        self.boardPin = boardPin

    def setup(self, shortPress, longPress):
        i2c = board.I2C() #i2c object from the SDA/SCL pins
        if self.pcf:
            pcfObj = adafruit_pcf8547.PCF8574(i2c, 0x20) #Save the IO expander as an object with an address of 0x20 (all address pins to ground)
            digitalInOutPin = pcfObj.get_pin(self.pin)
        else:
            digitalInOutPin = DigitalInOut(self.boardPin)

        digitalInOutPin.direction = Direction.INPUT
        digitalInOutPin.pull = Pull.UP
        return Button(digitalInOutPin, shortPress, longPress, True)