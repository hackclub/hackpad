# SPDX-FileCopyrightText: 2022 Scott Shawcroft for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Example demonstrating how to set the realtime clock (RTC) based on NTP time."""

import os
import time

import rtc
import socketpool
import wifi

import adafruit_ntp

# Get wifi AP credentials from a settings.toml file
wifi_ssid = os.getenv("CIRCUITPY_WIFI_SSID")
wifi_password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
if wifi_ssid is None:
    print("WiFi credentials are kept in settings.toml, please add them there!")
    raise ValueError("SSID not found in environment variables")

try:
    wifi.radio.connect(wifi_ssid, wifi_password)
except ConnectionError:
    print("Failed to connect to WiFi with provided credentials")
    raise

pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=0, cache_seconds=3600)

# NOTE: This changes the system time so make sure you aren't assuming that time
# doesn't jump.
rtc.RTC().datetime = ntp.datetime

while True:
    print(time.localtime())
    time.sleep(1)
