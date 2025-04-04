import usb_hid

keyboard_report_descriptor = bytes((
    0x05, 0x01,
    0x09, 0x06,
    0xA1, 0x01,
    0x05, 0x07,
    0x19, 0xE0,
    0x29, 0xE7,
    0x15, 0x00,
    0x25, 0x01,
    0x75, 0x01,
    0x95, 0x08,
    0x81, 0x02,
    0x95, 0x01,
    0x75, 0x08,
    0x81, 0x01,
    0x95, 0x06,
    0x75, 0x08,
    0x15, 0x00,
    0x25, 0x65,
    0x05, 0x07,
    0x19, 0x00,
    0x29, 0x65,
    0x81, 0x00,
    0xC0,
))

keyboard = usb_hid.Device(
    report_descriptor=keyboard_report_descriptor,
    usage_page=0x01,
    usage=0x06,
    report_ids=(0,),
    in_report_lengths=(8,),
    out_report_lengths=(0,)
)

usb_hid.enable((keyboard,))

class Keyboard:
    def __init__(self):
        self.report = bytearray(8)
        self.pressed_keys = set()
        self.current_layer = 0
        
    def clear_all(self):
        for i in range(8):
            self.report[i] = 0
        self.pressed_keys = set()
        
    def add_keycode(self, keycode, modifier=0):
        if keycode == 0:
            return False
            
        if keycode >= 0xF0:
            if keycode == 0xF0:
                self.current_layer = 1
            return True
            
        if keycode <= 0xE7 and keycode >= 0xE0:
            self.report[0] |= 1 << (keycode - 0xE0)
            return True
            
        for i in range(2, 8):
            if self.report[i] == 0:
                self.report[i] = keycode
                self.pressed_keys.add(keycode)
                return True
                
        return False
        
    def remove_keycode(self, keycode, modifier=0):
        if keycode == 0:
            return False
            
        if keycode >= 0xF0:
            if keycode == 0xF0:
                self.current_layer = 0
            return True
            
        if keycode <= 0xE7 and keycode >= 0xE0:
            self.report[0] &= ~(1 << (keycode - 0xE0))
            return True
            
        for i in range(2, 8):
            if self.report[i] == keycode:
                self.report[i] = 0
                if keycode in self.pressed_keys:
                    self.pressed_keys.remove(keycode)
                self._repack_report()
                return True
                
        return False
        
    def _repack_report(self):
        temp_report = bytearray(8)
        temp_report[0] = self.report[0]
        temp_report[1] = self.report[1]
        
        index = 2
        for i in range(2, 8):
            if self.report[i] != 0:
                temp_report[index] = self.report[i]
                index += 1
                
        self.report = temp_report
        
    def send(self):
        try:
            usb_hid.send_report(self.report, keyboard)
        except:
            pass
