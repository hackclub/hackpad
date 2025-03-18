# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""VCNL4200 Full Test"""

import time

import board
import busio

from adafruit_vcnl4200 import LED_I, PS_INT, Adafruit_VCNL4200

i2c = board.I2C()
sensor = Adafruit_VCNL4200(i2c)

print(" '''ALS Settings''' ")
print(f"Lux Persistence Mode: {sensor.als_persistence}")
print(f"Lux Integration Mode: {sensor.als_integration_time}")
print(f"Lux Persistence Mode: {sensor.als_persistence}")
sensor.als_threshold_low = 0
print(f"Lux Low Threshold: {sensor.als_low_threshold}")
sensor.als_threshold_high = 500
print(f"Lux High Threshold: {sensor.als_high_threshold}")

print(" '''Proximity Settings''' ")
sensor.prox_interrupt = PS_INT["BOTH"]
print(f"Proximity Interrupt Mode: {sensor.prox_interrupt}")
sensor.prox_interrupt_logic_mode = False
print(f"Proximity Interrupt Logic Mode: {sensor.prox_interrupt_logic_mode}")
sensor.prox_int_threshold_low = 0
print(f"Proximity Threshold Low: {sensor.prox_int_threshold_low}")
sensor.prox_int_threshold_high = 500
print(f"Proximity Threshold High: {sensor.prox_int_threshold_high}")
sensor.prox_active_force = False
print(f"Proximity Active Force: {sensor.prox_active_force}")
sensor.prox_smart_persistence = False
print(f"Proximity Smart Persistence: {sensor.prox_smart_persistence}")
sensor.prox_led_current = LED_I["50MA"]
print(f"Proximity IR LED Current: {sensor.prox_led_current}")
sensor.prox_cancellation_level = 0
print(f"Proximity Cancellation Level: {sensor.prox_cancellation_level}")
print(f"Proximity Integration Mode: {sensor.prox_integration_time}")
print(f"Proximity Persistence Mode: {sensor.prox_persistence}")
print(f"Proximity Duty Cycle: {sensor.prox_duty}")

print(" '''Proximity Sunlight Settings''' ")
print(f"Sun Protect Polarity: {sensor.sun_protect_polarity}")
sensor.prox_boost_typical_sunlight_capability = False
print(
    f"Proximity Boost Typical Sunlight Capability: {sensor.prox_boost_typical_sunlight_capability}"
)
sensor.prox_sun_cancellation = False
print(f"Proximity Sun Cancellation: {sensor.prox_sun_cancellation}")
sensor.prox_sunlight_double_immunity = False
print(f"Proximity Sunlight Double Immunity: {sensor.prox_sunlight_double_immunity}")

print(f"Interrupt Flags: {sensor.interrupt_flags}")
print(f"Proximity is: {sensor.proximity}")
print(f"Ambient is: {sensor.lux}")

while True:
    pass
