import time
import board
import digitalio
from rainbowio import colorwheel

class LEDManager:
    def __init__(self, rgb_pixels):
        self.pixels = rgb_pixels
        self.color_cycle = 0
        self.last_update = time.monotonic()
        self.update_interval = 0.05
        
        self.mute_led = digitalio.DigitalInOut(board.D9)
        self.mute_led.direction = digitalio.Direction.OUTPUT
        self.deafen_led = digitalio.DigitalInOut(board.D10)
        self.deafen_led.direction = digitalio.Direction.OUTPUT
        
        self.is_muted = False
        self.is_deafened = False

    def update_chain(self):
        current = time.monotonic()
        if current - self.last_update > self.update_interval:
            for i in range(4):
                color_index = (self.color_cycle + (i * 64)) % 255
                self.pixels[i] = colorwheel(color_index)
            self.color_cycle = (self.color_cycle + 1) % 255
            self.pixels.show()
            self.last_update = current

    def toggle_mute(self):
        self.is_muted = not self.is_muted
        self.mute_led.value = self.is_muted

    def toggle_deafen(self):
        self.is_deafened = not self.is_deafened
        self.deafen_led.value = self.is_deafened
        if self.is_deafened:
            self.is_muted = True
            self.mute_led.value = True
