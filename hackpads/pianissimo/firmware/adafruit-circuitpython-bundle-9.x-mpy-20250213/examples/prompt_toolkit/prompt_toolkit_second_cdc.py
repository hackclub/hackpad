# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

# This example works over the second CDC and supports history.

import usb_cdc

# Rename import to make the rest of the code compatible with CPython's prompt_toolkit library.
import adafruit_prompt_toolkit as prompt_toolkit

# If the second CDC is available, then use it instead.
serial = usb_cdc.console
if usb_cdc.data:
    serial = usb_cdc.data

session = prompt_toolkit.PromptSession(input=serial, output=serial)

while True:
    response = prompt_toolkit.prompt("$ ")
    print("->", response, file=serial)
