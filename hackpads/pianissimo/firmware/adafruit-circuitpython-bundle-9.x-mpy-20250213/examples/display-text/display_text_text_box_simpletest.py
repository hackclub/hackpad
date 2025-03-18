# SPDX-FileCopyrightText: 2024 foamyguy for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import displayio
import terminalio
from adafruit_display_text.text_box import TextBox

main_group = displayio.Group()

left_text = ("Left left left left " * 2).rstrip()
left_text_area = TextBox(
    terminalio.FONT,
    190,
    TextBox.DYNAMIC_HEIGHT,
    align=TextBox.ALIGN_LEFT,
    text=left_text,
    background_color=0xFF00FF,
    color=0x000000,
    scale=1,
)

left_text_area.x = 10
left_text_area.y = 10
main_group.append(left_text_area)


center_text = ("center center center " * 2).rstrip()
center_text_area = TextBox(
    terminalio.FONT,
    190,
    TextBox.DYNAMIC_HEIGHT,
    align=TextBox.ALIGN_CENTER,
    text=center_text,
    background_color=0x00FF00,
    color=0x000000,
    scale=1,
)

center_text_area.x = 10
center_text_area.y = 10 + left_text_area.height + 10
main_group.append(center_text_area)


right_text = ("right right right right " * 2).rstrip()
right_text_area = TextBox(
    terminalio.FONT,
    190,
    TextBox.DYNAMIC_HEIGHT,
    align=TextBox.ALIGN_RIGHT,
    text=right_text,
    background_color=0xFFFF00,
    color=0x000000,
    scale=1,
)

right_text_area.x = 10
right_text_area.y = center_text_area.y + center_text_area.height + 10
main_group.append(right_text_area)

board.DISPLAY.root_group = main_group
while True:
    pass
