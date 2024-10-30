import board #Allows for access to the board's systems
from digitalio import DigitalInOut, Direction, Pull #Allows for digital I/O access
import adafruit_pcf8547 #I/O expander library
from adafruit_debouncer import Button #Button presses
import rotaryio #For encoder

class enc:
    def __init__ (self, pcfPin1=None, pcfPin2=None, pcf=False, boardPin1=None, boardPin2=None):
        self.pcfPin1 = pcfPin1
        self.pcfPin2 = pcfPin2
        self.pcf = pcf
        self.boardPin1 = boardPin1
        self.boardPin2 = boardPin2

    def setup(self):
        i2c = board.I2C() #i2c object from the SDA/SCL pins
        if self.pcf:
            pcfObj = adafruit_pcf8547.PCF8574(i2c, 0x20) #Save the IO expander as an object with an address of 0x20 (all address pins to ground)
            digitalInOutPin1 = pcfObj.get_pin(self.pcfPin1)
            digitalInOutPin2 = pcfObj.get_pin(self.pcfPin2)
        else:
            digitalInOutPin1 = DigitalInOut(self.boardPin1)
            digitalInOutPin2 = DigitalInOut(self.boardPin2)

        return rotaryio.IncrementalEncoder(digitalInOutPin1, digitalInOutPin2)