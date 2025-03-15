# The Split56

My hackboard was designed to help make typing more comfortable for me. The board layout was made through iteration, printing out a scale picture of the pcb and testing it in real life. It fits my had perfectly and helps reduce strain on my hands while typing.
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/2f31fc919d3ddfc09d30a4ed8ce8654bb562c718_assembly_1__2_.png)

## Features:
- 56 keys including a num row and a thumb cluster
- 2 rotary encoders
- 2 Oled Screens
- RGB Underglow
- RGB Status Light

# PCB

The Split56 PCB was designed using KiCad.
## Schematic

Dont mind the bad practices 😁
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/13a022dc52296590888314819d4f722f4c52c5f0_image.png)

## PCB

oooh! rounded traces!
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/82c6aae2492a04781b626e117a0441a22da5ce65_image.png)

# Case

I designed the case in onshape. I was going for a very minimalist design with the bare board. There is a ring on the bottom of the plate to mount some tenting feet
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ab100534b134541cb4f8936fc03646c4128a3b2a_assembly_1__3_.png)

# Firmware

This board is powered on KMK. I used pog to help with some of the keymapping stuff.

# BOM

| Item              | Quantity | Induvidual Price |
| :---------------- | :------: | ----: |
| PCB Left |   1   | ~ $12.40 |
| PCB Right |   1   | ~ $12.40 |
| Orpheus Pico | 2 | N/A |
| [OLED Screen](https://www.aliexpress.us/item/3256807215355950.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%2010.43%21USD%205.21%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000040595474264%21ct%21US%21-1%21%211%210&_gl=1*yzm11q*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MTk5NzEwMC4zMi4xLjE3NDE5OTg1NjEuMTQuMC4w&gatewayAdapt=glo2usa) |  2   | $1.04 |
| [Rotary Endcoder](https://www.aliexpress.us/item/2251832789732148.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%203.21%21USD%203.21%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000025499862671%21ct%21US%21-1%21%211%210&_gl=1*hzx562*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4wLjE3NDIwMDA5NzUuNjAuMC4w&gatewayAdapt=glo2usa) |  2   | $0.32 |
| [100x Diodes](https://www.aliexpress.com/item/2255799955957794.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%201.14%21USD%201.14%21%21%21%21%21%402101c5a417419970984615902e4a1a%2110000000428321629%21ct%21US%21-1%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D&_gl=1*10vdffy*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4xLjE3NDIwMDEwNTIuNjAuMC4w) | 1 | $1.14 |
| [USB-C Ports](https://www.aliexpress.com/item/3256803863526495.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%203.43%21USD%203.43%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000027860863313%21ct%21US%21-1%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D&_gl=1*u7z71h*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4xLjE3NDIwMDEwNTIuNjAuMC4w) | 2 | $0.69 |
| [18x Linear Switches](https://divinikey.com/products/haimu-x-geon-hg-black-linear-switches?variant=40373069545537) | 4 | $5.40/pack $0.30/switch |
| [100x Hot Swap Sockets](https://www.aliexpress.com/item/3256807522919795.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%206.52%21USD%200.99%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000041931656046%21ct%21US%21-1%21%211%210&_gl=1*14jr3r4*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4xLjE3NDIwMDEwNTIuNjAuMC4w) | 1 | $6.52 |
| [Switch Foams (optional)](https://divinikey.com/products/kbdfans-switch-pads?variant=39400489254977) | 1 | $5.90 |
| [Keycaps](https://www.amazon.com/Keycaps-MOA-Keyboard-Sublimation-Switches-Keyboards/dp/B0DB21SWLC?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A157804XWFVRE0&gPromoCode=17253097989582193996&gQT=1&th=1) | 1 | $24.02 |
| Acrylic Left | 1 | N/A |
| Acrylic Right | 1 | N/A |
| 3D Printed Tenting Base | 2 | N/A |
| [M2x3 Heat-Set Inserts](https://www.aliexpress.us/item/3256807155790358.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%201.00%21USD%200.85%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000040339692937%21ct%21US%21-1%21%211%210&_gl=1*ck4p8m*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4xLjE3NDIwMDE0NTIuNjAuMC4w&gatewayAdapt=glo2usa) | 34 | $0.02 |
| [100x M2x8mm Bolts](https://www.aliexpress.us/item/3256802227337773.html?spm=a2g0o.cart.0.0.10db38da9BcJ7N&mp=1&pdp_npi=5%40dis%21USD%21USD%201.41%21USD%201.41%21%21%21%21%21%402101c5a417419970984615902e4a1a%2112000034223710446%21ct%21US%21-1%21%211%210&pdp_ext_f=%7B%22cart2PdpParams%22%3A%7B%22pdpBusinessMode%22%3A%22retail%22%7D%7D&_gl=1*3u9kjb*_gcl_aw*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_dc*R0NMLjE3NDE2NTExOTUuQ2owS0NRandtN3EtQmhEUkFSSXNBQ0Q2LWZVRTVsMWIzTDVQTjRsb0tlMTI5YTh1clV6RWlXQWRtdEo4bXZvckljRTJtazFLajdSSXhfNGFBdng5RUFMd193Y0I.*_gcl_au*MTc3ODkyNTc1LjE3MzY2MDg1Mzk.*_ga*MTg5MDU3ODUzMS4xNzM1NTMwNjQx*_ga_VED1YSGNC7*MTc0MjAwMDk3NS4zMy4xLjE3NDIwMDE2NTkuNjAuMC4w&gatewayAdapt=glo2usa) | 1 | $1.41 |
