# KiCad Libraries

Set of symbols/footprints/models that I've created for my projects.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/sszczep)

###### I'm not taking responsibility for any mistakes that I could have made. Be sure to double check all the dimensions and wiring before using in projects. 

## How to use

Download footprints (***.pretty** directories) and symbols (***.lib** files) that you want to use and add them as global or project specific libraries. To use 3D Models, you must create **SSZCZEP_MODELS** environment variable pointing to **models** directory.

## Symbols

### CherryMX.lib

Name | Description | Preview
---- | ----------- | -------
CherryMX | Just a regular Cherry MX switch | ![CherryMX](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/SYMBOL-CherryMX.jpg)
CherryMX_LED | Cherry MX switch with THT LED | ![CherryMX_LED](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/SYMBOL-CherryMX_LED.jpg)
CherryMX_LTST-A683CEGBW | Cherry MX switch with LTST-A683CEGBW for underglow | ![CherryMX_LTST-A683CEGBW](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/SYMBOL-CherryMX_LTST-A683CEGBW.jpg)

## Footprints

### CherryMX[variant].pretty

Nearly 600 different footprints for Cherry MX switches generated using [this](https://github.com/sszczep/kicad-libraries/blob/master/footprints/generateCherryMX.py) code. 

It includes variants such as:
* Plate/PCB mounted
* Stabilizer Plate/PCB mounted
* No LED/2 pin LED/LTST-A683CEGBW
* Normal switch mount/Kailh Socket for hot-swap compatibility

Example footprints:

![CherryMX_1.00u_PCB](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/FOOTPRINT-CherryMX_1.00u_PCB.jpg) | ![CherryMX_1.00u_PCB_KailhSocket_LTST-A683CEGBW](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/FOOTPRINT-CherryMX_1.00u_PCB_KailhSocket_LTST-A683CEGBW.jpg) | ![CherryMX_2.00u_PCB_Stab](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/FOOTPRINT-CherryMX_2.00u_PCB_Stab.jpg)
---|---|---

## 3D Models

Name | Description | Preview
---- | ----------- | -------
LTST-A683CEGBW | Reverse mounted RGB SMD LED that I use for underglowing Cherry MX switches. Detailed datasheet can be found [here](https://optoelectronics.liteon.com/upload/download/DS35-2019-0032/LTST-A683CEGBW.PDF). | ![LTST-A683CEGBW](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/MODEL-LTST-A683CEGBW.jpg)
KailhSocket | This model was obtained from [*QMK*](https://github.com/qmk). All credits go to them. The exact file can be found [here](https://github.com/qmk/qmk_hardware/blob/master/components/kailh_socket_mx.stp). I'm keeping it here as it is easier to link and use in all of my projects. | ![KailhSocket](https://raw.githubusercontent.com/sszczep/kicad-libraries/media/MODEL-KailhSocket.jpg)
