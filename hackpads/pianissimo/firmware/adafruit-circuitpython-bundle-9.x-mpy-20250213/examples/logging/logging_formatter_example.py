# SPDX-FileCopyrightText: 2024 Tim Cocks
# SPDX-License-Identifier: MIT


"""Illustrate usage of default and custom Formatters including
one with timestamps."""

import adafruit_logging as logging

# To test on CPython, un-comment below and comment out above
# import logging


logger = logging.getLogger("example")
logger.setLevel(logging.INFO)
print_handler = logging.StreamHandler()
logger.addHandler(print_handler)

default_formatter = logging.Formatter()

print_handler.setFormatter(default_formatter)
logger.info("Default formatter example")


timestamp_formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s: %(message)s")
print_handler.setFormatter(timestamp_formatter)
logger.info("Timestamp formatter example")


custom_vals_formatter = logging.Formatter(
    fmt="%(ip)s %(levelname)s: %(message)s", defaults={"ip": "192.168.1.188"}
)
print_handler.setFormatter(custom_vals_formatter)
logger.info("Custom formatter example")


bracket_timestamp_formatter = logging.Formatter(
    fmt="{asctime} {levelname}: {message}", style="{"
)
print_handler.setFormatter(bracket_timestamp_formatter)
logger.info("Timestamp formatter bracket style example")


bracket_custom_vals_formatter = logging.Formatter(
    fmt="{ip} {levelname}: {message}", style="{", defaults={"ip": "192.168.1.188"}
)
print_handler.setFormatter(bracket_custom_vals_formatter)
logger.info("Custom formatter bracket style example")
