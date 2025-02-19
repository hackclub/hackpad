# SPDX-FileCopyrightText: Copyright (c) 2025 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_lps28

i2c = board.I2C()
sensor = adafruit_lps28.LPS28(i2c)

# Data Rate in hz
# 1, 4, 10, 25, 50, 75, 100 or 200 (default)
# sensor.data_rate = 200

# Number of samples to average per measurement
# 4 (default), 8, 16, 32, 64, 128, 512
# sensor.averaging = 4

# Full scale measurement mode for pressure
# (False = 1260 hPa, True = 4060 hPa (default))
# sensor.full_scale_mode = True

# Enable/Disable Interrupts Defaults

# sensor.data_ready_int = True # Data Ready Interrupt
# sensor.data_ready_pulse = False # Data-ready interrupt as a pulse
# sensor.fifo_full_int = False # FIFO full interrupt
# sensor.fifo_overrun_int = False # FIFO overrun interrupt
# sensor.fifo_watermark_int = False # FIFO watermark interrupt

print("LPS28 Simple Test")
print("-" * 40)

while True:
    if sensor.data_ready:
        print(f"Pressure: {sensor.pressure:.1f} hPa")
        print(f"Temperature: {sensor.temperature:.1f} °C")
        print("-" * 40)

    time.sleep(0.5)
