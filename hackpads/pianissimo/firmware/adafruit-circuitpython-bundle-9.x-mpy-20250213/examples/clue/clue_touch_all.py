# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""This example prints to the serial console when you touch the capacitive touch pads."""
import time
import board
from adafruit_clue import clue


# You'll need to first use the touchpads individually to register them as active touchpads
# You don't have to use the result though
is_p0_touched = clue.touch_0  # This result can be used if you want
if is_p0_touched:
    print("P0/D0 was touched upon startup!")
is_p1_touched = clue.touch_1
is_p2_touched = clue.touch_2


print("Pads that are currently setup as touchpads:")
print(clue.touch_pins)

while True:
    current_touched = clue.touched

    if current_touched:
        print("Touchpads currently registering a touch:")
        print(current_touched)
    else:
        print("No touchpads are currently registering a touch.")

    if all(pad in current_touched for pad in (board.P0, board.P1, board.P2)):
        print("This only prints when P0, P1, and P2 are being held at the same time!")

    time.sleep(0.25)
