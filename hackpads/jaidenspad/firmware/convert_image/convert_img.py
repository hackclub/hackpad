import cv2 
import sys

# usage: python3 convert_img.py <path_to_image>
# your image should be black and white
# it MUST be 128x32 pixels (for it to work correctly)

dir = sys.argv[1]

img = cv2.imread(dir, 0)


height, width = img.shape

a = ""
b = ""

fx = -1
lx = -1

# go through pixel by pixel
for x in range(0, width):
    for y in range(0, height):
        if y % 8 == 0:
            a += " "
            if y > 0:
                b += ", 0b"

        if x % 1 == 0 and y == 0:
            a += "\n"
            b += ", \n0b"

        if img[y][x] == 0:
            a += "1"
            b += "1"
            if fx == -1:
                fx = x + 1 - 1
                print("first index: ", fx)
            lx = x + 1 - 1
            print("last index: ", lx)
        else:
            a += "█"
            b += "0"

print(a)

b = b[3:len(b)]

llx = lx + 2
if llx > width:
    llx = width

ffx = fx - 1
if ffx < 0:
    ffx = 0

print(ffx, llx)
print(len(b.split("\n")))

b = '\n\t'.join(b.split("\n")[ffx:llx])
print("const unsigned char PROGMEM image[] = {")
print('\t' + b[0:len(b)-2])
print("};")
print("starts at line: ", ffx)
h = b[0:len(b)-2].split("\n")
print("height: ", len(h))