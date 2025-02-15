
# Tango's Hackpad

Tango's Hackpad is a 15 key macropad with a rotary encoder, and uses QMK firmware

## Features:

- 3 Layer sandwitch case
- EC11 Rotary encoder
- 15 Keys
- QMK programable
- 2 PCB design making it smaller in X and Y distance
- 5 degree tilted angle

## CAD Model:

Everything fits together using 2x M2x20, 1x m2x18, 2x m2x14 Bolts. Also, it has a 5 degree tilt

It has 13 separate printed pieces 10 are spacers and the rest 3 are the case. The angle, the middle part that covers the bottom of the PCB, and the plate that covers the top, and the spacers.

![[Screenshot 2025-02-14 150812.png]]
![[Screenshot 2025-02-14 150819.png]]
![[Screenshot 2025-02-14 150834.png]]
Made in Fusion.

## PCB

Here's my PCB! It was made in KiCad..

Schematic
![[ksnip_20250215-115903.png]]

PCB
![[ksnip_20250215-115938.png]]

## Firmware Overview

This hackpad uses [QMK](https://qmk.fm/) firmware for everything.

- the rotary encoder does nothing at the moment but is programmable to your desire.
- The 15 keys currently have the alphabet programmed but can be easily changed in keymap.c   

## BOM:

Here should be everything you need to make this hackpad

- 15x Cherry MX style switches
- 15x DSA Keycaps
- 2x m2x20 bolts
- 1x m2x18 bolt
- 2x m2x14 bolts
- 5x m2 nuts
- 16x 1N4148 DO-35 Diodes.
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (13 printed parts)
- 2x header 7 pin
- 11x wires min length 2cm

## Extra stuff

### Screw type
exact screw im using:  [HERE](https://pt.aliexpress.com/item/1005002254557923.html?spm=a2g0o.productlist.main.3.6077u9Qnu9QnaL&algo_pvid=bb7ceba6-37ee-42ab-99b2-a6a36aa1285a&algo_exp_id=bb7ceba6-37ee-42ab-99b2-a6a36aa1285a-1&pdp_ext_f=%7B%22order%22%3A%221261%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis!EUR!1.63!0.97!!!1.67!1.00!%40211b441e17395529998376835e9035!12000019667348276!sea!PT!0!ABX&curPageLogUid=ef7irWHSBfqs&utparam-url=scene%3Asearch%7Cquery_from%3A)
![[Pasted image 20250215112550.png]]
