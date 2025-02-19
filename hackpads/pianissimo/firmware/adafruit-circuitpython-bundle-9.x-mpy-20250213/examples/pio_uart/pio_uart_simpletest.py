# SPDX-FileCopyrightText: Copyright (c) 2023 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

import board
import adafruit_pio_uart

uart = adafruit_pio_uart.UART(board.TX, board.RX)

uart.write(b"\x00")
print(uart.read(1))
