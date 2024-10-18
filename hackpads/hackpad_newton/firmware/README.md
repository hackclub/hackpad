# Firmware Hackpad Newton

## upload to MCU
- get a python environment with mpremote `pip install mpremote`
- install the used mip packages on the mcu
  - `mpremote mip install github:mcauser/micropython-pcf8574`
  - `mpremote mip install github:josverl/micropython-stubs/mip/typing.py`
  - `mpremote mip install usb-device-keyboard`
  - `mpremote mip install github:anatol-newton/micropython-ili9225`
  - `mpremote mip install github:anatol-newton/micropython-stc31c`
- upload `main.py` to the device
- done!

## Development Setup

To get code completion and stuff (this only works on linux systems):

- get yourself the micropython unix port and build it
- copy the executable to some place your system knows to look for executables in
- set the micropython path environment variable like this (while being in the root folder of the firmware)
    - `export MICROPYPATH=":.micropython/lib:.frozen"`
- install the used micropython packages
    - `micropython -m mip install --no-mpy github:mcauser/micropython-pcf8574`
    - `micropython -m mip install --no-mpy github:josverl/micropython-stubs/mip/typing.py`
    - `micropython -m mip install --no-mpy usb-device-keyboard`
    - `micropython -m mip install --no-mpy github:anatol-newton/micropython-ili9225`
    - `micropython -m mip install --no-mpy github:anatol-newton/micropython-stc31c`
- set the folders `src` and `.micropython/lib` as source folders (if you are using pycharm, this should be configured
  already)
- create a new python venv and activate it
- install other default packages for micropython code completion (again, when using pycharm, install the micropython
  plugin and activate micropython for this project, then it'll automatically tell you to install the missing packages)
  - ```txt 
    adafruit-ampy==1.0.7
    click==8.1.7
    docopt==0.6.2
    pyserial==3.5
    python-dotenv==1.0.1
    ```
- now you should have code completion and stuff :D
