import analogio, board, digitalio, usb_cdc
from array import array

# I/O initialization
owsi_in = analogio.AnalogIn (board.A0)
kbclk = digitalio.DigitalInOut (board.D1)
kbclk.switch_to_output ()
kb0 = digitalio.DigitalInOut (board.D2)
kb0.switch_to_input (pull = digitalio.Pull.DOWN)
kb1 = digitalio.DigitalInOut (board.D3)
kb1.switch_to_input (pull = digitalio.Pull.DOWN)
gp2 = digitalio.DigitalInOut (board.D4)
gp2.switch_to_output ()
gp1 = digitalio.DigitalInOut (board.D5)
gp1.switch_to_output ()
gp0 = digitalio.DigitalInOut (board.D6)
gp0.switch_to_output ()
owsi_pd = digitalio.DigitalInOut (board.D7)
owsi_pd.switch_to_output ()
owsi_wpu = digitalio.DigitalInOut (board.D8)
owsi_wpu.switch_to_output ()
owsi_spu = digitalio.DigitalInOut (board.D9)
owsi_spu.switch_to_output ()

serial = usb_cdc.data

# Quadrature encoder
# 0: No change; 1: Forward; -1: Backward, 2: Error
# Keys: Decimal value of (A, B, A', B')
enc_a, enc_b = 2, 0
enc_ttable = array ("b", (
    0, -1, 1, 2,
    1, 0, 2, -1,
    -1, 2, 0, 1,
    2, 1, -1, 0,
    0, 0, 0, 0
))

def read_kb ():
    keys = array ("b", (0, ) * 11)
    enc = array ("b")
    for i in (0, 5):
        keys [i] = kb0.value
        enc_a1 = kb1.value
        kbclk.value = True
        kbclk.value = False
        keys [i + 1] = kb0.value
        enc_b1 = kb1.value
        enc.append (enc_ttable [enc_a << 3 | enc_b << 2 | enc_a1 << 1 | enc_b1])
        kbclk.value = True
        kbclk.value = False
        keys [i + 2] = kb0.value
        keys [{0: 12, 5: 11} [i]] = kb1.value
        kbclk.value = True
        kbclk.value = False
        keys [i + 3] = kb0.value
        if kb1.value:
            raise ValueError ("Key matrix error") # TODO: Error handling
        kbclk.value = True
        kbclk.value = False
        keys [i + 4] = kb0.value
        if kb1.value:
            raise ValueError ("Key matrix error")
        kbclk.value = True
        kbclk.value = False
    return keys, enc

def owsi ():
    """
    This is a simple subset of the OWSI protocol which just passes data continuously between two devices.
    It is ultimately used to control up to 16 smart home devices with a focus on switches and dimmers.
    """
    pass

def main ()
    while True:
        keys, enc = read_kb ()
        serial.write (keys)
        serial.write (enc)
        serial.write (owsi ())
