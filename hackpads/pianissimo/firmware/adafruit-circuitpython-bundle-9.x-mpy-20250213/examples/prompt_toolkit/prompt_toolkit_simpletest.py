# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

# Rename import to make the rest of the code compatible with CPython's prompt_toolkit library.
import adafruit_prompt_toolkit as prompt_toolkit

# This basic example doesn't do much more than input but it's where to start.
while True:
    response = prompt_toolkit.prompt("$ ")
    print("->", response)
