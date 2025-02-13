# SPDX-FileCopyrightText: 2024 Jeff Epler, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""A PIO demo that uses the FIFO in random access mode

Random access mode is a new feature of the PIO peripheral of the RP2350.
This demo is not compatible with the original RP2040 or Raspberry Pi
Pico.

Wiring:
 * LED with current limiting resistor on GP25 (Pico 2 standard location)

The LED will blink in several patterns depending on the values loaded in the 'rxfifo' registers
"""

import array
import time
import board
import rp2pio
import adafruit_pioasm

program = adafruit_pioasm.Program(
    """
    .pio_version 1
    .set 1
    .fifo txget

    ; LED on time taken from rxfifo[0]
    mov osr, rxfifo[0]
    mov x, osr

    set pins, 1
xloop1:
    jmp x--, xloop1

    ; LED off time taken from rxfifo[1]
    mov osr, rxfifo[1]
    mov x, osr

    set pins, 0
xloop2:
    jmp x--, xloop2
    """
)


def assign_uint32s(ar, off, *args):
    """Assign multiple 32-bit registers within an AddressRange"""
    vv = b"".join(v.to_bytes(4, "little") for v in args)
    ar[off : off + 4 * len(args)] = vv


print(program.pio_kwargs)
sm = rp2pio.StateMachine(
    program.assembled,
    first_set_pin=board.GP25,
    frequency=10_000_000,
    **program.pio_kwargs,
)
fifo = sm.rxfifo

# Set non-zero register entries & re-start the state machine at its offset.
# this is needed because the default register value could represent a very long delay
fifo[0:4] = b"\1\0\0\0"
fifo[4:8] = b"\1\0\0\0"
sm.run(array.array("H", [sm.offset]))

while True:
    # equal blinks
    assign_uint32s(fifo, 0, 2000000, 2000000)
    time.sleep(1)

    # small on time
    assign_uint32s(fifo, 0, 1000000, 3000000)
    time.sleep(1)

    # small off time
    assign_uint32s(fifo, 0, 3000000, 1000000)
    time.sleep(1)

    # slower blinks
    assign_uint32s(fifo, 0, 3000000, 3000000)
    time.sleep(1)
