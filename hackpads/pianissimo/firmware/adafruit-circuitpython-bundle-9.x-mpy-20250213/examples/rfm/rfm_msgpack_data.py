# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to send a msgpack'd data packet periodically
# Author: Jerry Needell, Tim Cocks
#
import time
from io import BytesIO

import board
import busio
import digitalio
import msgpack

# Dictionary object that we will msgpack and send over the radio
payload_obj = {"counter": 0, "list": [True, False, None, 1, 3.14], "str": "CircuitPython is Fun!"}

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.D10)
RESET = digitalio.DigitalInOut(board.D11)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
# uncommnet the desired import and rfm initialization depending on the radio boards being used

# Use rfm9x for two RFM9x radios using LoRa

# from adafruit_rfm import rfm9x

# rfm = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Use rfm9xfsk for two RFM9x radios or RFM9x to RFM69 using FSK

from adafruit_rfm import rfm9xfsk

rfm = rfm9xfsk.RFM9xFSK(spi, CS, RESET, RADIO_FREQ_MHZ)

# Use rfm69 for two RFM69 radios using FSK

# from adafruit_rfm import rfm69

# rfm = rfm69.RFM69(spi, CS, RESET, RADIO_FREQ_MHZ)

# For RFM69 only: Optionally set an encryption key (16 byte AES key). MUST match both
# on the transmitter and receiver (or be set to None to disable/the default).
# rfm.encryption_key = None
# rfm.encryption_key = (
#    b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
# )

# for OOK on RFM69 or RFM9xFSK
# rfm.modulation_type = 1

# uncommnet to Disable the RadioHead  Header
# rfm.radiohead = False

# in FSK/OOK modes rfo RFM69 or RFM9X - addresss filtering may be enabled
# rfm.enable_address_filter=True
# rfm.fsk_node_address=0x2
# rfm.fsk_broadcast_address=0xff

# set the time interval (seconds) for sending packets
transmit_interval = 5

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm.tx_power = 23


# initialize counter
counter = 0

# Wait to receive packets.
print("Waiting for packets...")
# initialize flag and timer
send_reading = False
time_now = time.monotonic()
while True:
    # Look for a new packet - wait up to 2 seconds:
    packet = rfm.receive(timeout=2.0)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        print("Received (raw data): ", packet)

        try:
            # Unpack and print contents
            b = BytesIO()
            b.write(packet)
            b.seek(0)
            unpacked_msg = msgpack.unpack(b)
            print(f"Received (unpacked): {unpacked_msg}")
        except Exception as e:
            print("Unable to unpack message. Exception: ")
            print(e)

        # send reading after any packet received
    if time.monotonic() - time_now > transmit_interval:
        # reset timeer
        time_now = time.monotonic()
        # clear flag to send data
        send_reading = False
        counter = counter + 1

        b = BytesIO()
        payload_obj["counter"] = counter
        msgpack.pack(payload_obj, b)
        b.seek(0)
        rfm.send(b.read())
