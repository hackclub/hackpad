import board
from digitalio import DigitalInOut, Pull
from supervisor import ticks_ms

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import ShiftRegisterKeys

class ScooterMP(KMKKeyboard):
    def __init__(
        self,
        i2c,
        layers_names,
        ScooterMP_rgb=False,
        ScooterMP_oled=False,
        ScooterMP_modules=False
    ):
        # create and register the scanner
        self.matrix = ShiftRegisterKeys(
            # require arguments:
            clock=board.D1,
            data=board.D2,
            latch=board.D0,
            key_count=12,
            # optional arguments with defaults:
            value_to_latch=True, # 74HC165: True, CD4021: False
            value_when_pressed=False,
            interval=0.01,  # Debounce time in floating point seconds
            max_events=64
        )

        self.i2c = i2c
        self.layers_names = layers_names
        self.has_modules = ScooterMP_modules
        self.known_devices = []
        self.active_devices = []
        # debouncing variables
        self.polling_interval = 20
        self.last_tick = ticks_ms()
        # macropad settings
        self.set_rgb(ScooterMP_rgb)
        self.set_oled(ScooterMP_oled)
        self.set_interrupt(ScooterMP_modules)
         
    def set_rgb(self, ScooterMP_rgb):
        if ScooterMP_rgb:
            from kmk.extensions.RGB import RGB
            rgb = RGB(
                pixel_pin=board.D6,
                num_pixels=4,
                hue_default=80,
            )
            self.extensions.append(rgb)

    def set_oled(self, ScooterMP_oled):
        if ScooterMP_oled:
            from ScooterMP.display import ScooterMPDisplay, BitmapLogoScene, StatusScene

            scenes = [
                BitmapLogoScene("/firmware/scootersmp/logo.bmp"),
                StatusScene(layers_names=self.layers_names, separate_default_layer=False)
            ]
            self.oled = ScooterMPDisplay(self.i2c, scenes, width=128, height=32, rotation=180)
            self.extensions.append(self.oled)
    
    def set_interrupt(self, ScooterMP_modules):
        if ScooterMP_modules:
            self.interrupt = DigitalInOut(board.D7)
            self.interrupt.pull = Pull.UP

    def detect_interrupt(self):
        if not self.interrupt.value:
            self.draw_module_activity()
            return True
        return False
    
    def draw_module_activity(self):
        if hasattr(self, 'oled'):
            self.oled.draw_temp_arrow()

    def before_matrix_scan(self):
        super().before_matrix_scan()

        if not self.has_modules:
            return
                
        if self.detect_interrupt():
            self.process_active_modules()

    def process_active_modules(self):
        # Scan for active devices
        current_addresses = self.scan_i2c_addresses()

        # Process only modules that are both active and known
        for module in self.modules:
            if hasattr(module, 'i2c') and hasattr(module, 'addr'):
                if module.addr in current_addresses and module.addr in self.known_devices:
                    module.process_interrupt()
                else:
                    self.known_devices.append(module.addr)

    def scan_i2c_addresses(self):
        # Scan the I2C bus for connected devices
        if not self.i2c.try_lock():
            return
        try:
            found_addresses = self.i2c.scan()
            print("Found I2C devices at addresses:", [hex(addr) for addr in found_addresses])
            return found_addresses
        finally:
            self.i2c.unlock()

    coord_mapping = [
        8,  9,  10, 11,
        4,  5,   6,  7,
        0,  1,   2,  3,
    ]
