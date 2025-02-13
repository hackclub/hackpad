# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to send a packet periodically between addressed nodes
# Author: Jerry Needell
#
import time

import board
import busio
import digitalio

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
# uncommnet the desired import and rfm initialization depending on the radio boards being used

# Use rfm9x for two RFM9x radios using LoRa

from adafruit_rfm import rfm9x

rfm = rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Use rfm9xfsk for two RFM9x radios or RFM9x to RFM69 using FSK

# from adafruit_rfm import rfm9xfsk

# rfm = rfm9xfsk.RFM9xFSK(spi, CS, RESET, RADIO_FREQ_MHZ)

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

# set the time interval (seconds) for sending packets
transmit_interval = 2

# set node addresses
rfm.node = 1
rfm.destination = 100
# initialize counter
counter = 0
# send a broadcast message from my_node with ID = counter
rfm.send(bytes(f"Startup message {counter} from node {rfm.node}", "UTF-8"))

# Wait to receive packets.
print("Waiting for packets...")
now = time.monotonic()
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = rfm.receive(with_header=True, timeout=5.0)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print(f"Received (raw payload): {packet[4:]}")
        print(f"Received RSSI: {rfm.last_rssi}")
    if time.monotonic() - now > transmit_interval:
        now = time.monotonic()
        counter = counter + 1
        # send a  mesage to destination_node from my_node
        rfm.send(
            bytes(f"message number {counter} from node {rfm.node}", "UTF-8"),
            keep_listening=True,
        )
        button_pressed = None
