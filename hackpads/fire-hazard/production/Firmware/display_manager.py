import time
import random
from displayio import Group

class DisplayManager:
    def __init__(self, display, splash_group, media_info):
        self.display = display
        self.splash_group = splash_group
        self.media_info = media_info
        self.last_activity = time.monotonic()
        self.last_shift = time.monotonic()
        self.shift_interval = 30
        self.timeout = 600
        self.original_position = (splash_group.x, splash_group.y)

    def update(self):
        current_time = time.monotonic()

        if current_time - self.last_shift > self.shift_interval:
            self._shift_content()
            self.last_shift = current_time
        
        if current_time - self.last_activity > self.timeout:
            if "No track playing" in self.media_info.get_media_info():
                self.display.brightness = 0.1
            else:
                self.display.brightness = 1.0
        else:
            self.display.brightness = 1.0

    def register_activity(self):
        self.last_activity = time.monotonic()
        self.display.brightness = 1.0

    def _shift_content(self):
        self.splash_group.x = self.original_position[0] + random.randint(-2, 2)
        self.splash_group.y = self.original_position[1] + random.randint(-2, 2)
