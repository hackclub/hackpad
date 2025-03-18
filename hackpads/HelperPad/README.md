# HelperPad
by Jonas Heilig

## Description
This little HelperPed helps you to use shortcuts or enter often the same prepared text.<br>
You can easily change the text or shortcuts by changing the kb.py file.<br>
HelperPad is easily to use and customize.

## Parts of HelperPad
### Schematik
<img src="/hackpads/HelperPad/img/Shematic.png" width="800">

### PCB
<img src="/hackpads/HelperPad/img/PCB.png" width="800">

### Case
<img src="/hackpads/HelperPad/img/CAD1.png" width="800">
<img src="/hackpads/HelperPad/img/CAD2.png" width="800">
<img src="/hackpads/HelperPad/img/CAD3.png" width="800">

### Firmware
In kb.py you can define what each action should do.<br>
One action is a row of action like press a key like A; B; C; F1; ESC ...<br>
For each button you has one variable as action row, were you can define what each of the nine buttons should do.<br>
<br>
In main.py you can define the words the oled should show.<br>
The words are defined in 'messages'. They change every 7 seconds.<br>
They show up in the same order as they are defined in 'messages'.

## BOM

| #   | Value          | Reference                                    | Footprint                                         | Qty |
|-----|----------------|---------------------------------------------|-------------------------------------------------|-----|
| 1   | 1N4148         | D2, D3, D5, D6, D8, D9, D10, D12, D14       | Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal      | 9   |
| 2   | SW_Push        | SW1, SW2, SW3, SW4, SW5, SW6, SW7, SW8, SW9 | Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB   | 9   |
| 3   | XIAO-RP2040-DIP| U1                                          | OPL:XIAO-RP2040-DIP                             | 1   |
| 4   | DM-OLED091     | U3                                          | OLED_096:SSD1306-0.91-OLED-4pin-128x32         | 1   |
