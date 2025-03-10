# Meow70
![render](https://hc-cdn.hel1.your-objectstorage.com/s/v3/628a89b35572406577e7232d115b553968880ddb_keeb_render.png)

## Building the Board
My idea started with how I wanted a split keyboard that wasn't ortholinear or ergo. So, I took a picture of my Keychron K6 Pro, and designed a split keyboard off of it. It runs on 2 Raspberry Pi Picos (or drop in replacements) with a simple, open case design and qmk firmware.\
This was a pretty difficult build, I ended up redoing the routing and placement several times, going from a staggered edge with the controllers mounted underneath, to what I have today. The most difficult part was doing the render of the keyboard (which is still a WIP, this is just temporary). My KICAD always gave me destroyed meshes that would take hours to import into any software. Once I finally got something imported, it took me 2 days of constantly doing little things and saving my work before blender crashed. The final render took over 8 minutes to finish, so it was quite an undertaking getting it to work.

## Bill of Materials
* 1x set of pcbs
* 2x Raspberry Pi Pico H
* 69x Kailh Hotswap Sockets (MX Style)
* 69x 1N4148 Diodes
* 69x MX-Style Switches
* 4x Plate-Mounted Stabilizers
* 2x 0.91" I2C PCB-Mounted OLED Displays
* 2x TRRS Audio Jack Connectors
* 8x M3 Screws
* 8x M3 Heatset Inserts

## More Photos
![schematic](https://hc-cdn.hel1.your-objectstorage.com/s/v3/861ee88085adb3ed38c9c139cd76bb08c1c6f49c_screenshot_2025-03-09_154452.png)
![pcb](https://hc-cdn.hel1.your-objectstorage.com/s/v3/4fb86ea1f16ce5646c4538d2c452d8ba963b1977_screenshot_2025-03-09_154533.png)
![case](https://hc-cdn.hel1.your-objectstorage.com/s/v3/6bef63617453d71a1472ec37ec80bc572794aa9b_screenshot_2025-03-09_155011.png)