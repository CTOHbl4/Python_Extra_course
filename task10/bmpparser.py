import struct
import sys


a = b""
while c := sys.stdin.buffer.read():
    a += c
bmp = a

typ = bmp[:2].decode()
size = struct.unpack('I', bmp[2:6])[0]

DIB_size = struct.unpack('I', bmp[14:18])[0]
W = struct.unpack('I', bmp[18:22])[0]
H = struct.unpack('I', bmp[22:26])[0]
if W >= 0x80000000:
    W = 0x100000000 - W
if H >= 0x80000000:
    H = 0x100000000 - H
color_planes = struct.unpack('H', bmp[26:28])[0]
bits_per_pixel = struct.unpack('H', bmp[28:30])[0]
comp_meth = struct.unpack('I', bmp[30:34])[0]
raw_size = struct.unpack('I', bmp[34:38])[0]
add = (4-((W*bits_per_pixel//8) % 4)) % 4
calc_size = (W*bits_per_pixel//8 + add) * H

if typ != "BM":
    print("Not a Windows BMP")
    sys.exit()
if size != len(bmp):
    print("Incorrect size")
    sys.exit()
if DIB_size not in (12, 64, 16, 40, 52, 56, 108, 124):
    print("Incorrect header size")
    sys.exit()
if raw_size < calc_size:
    print("Incorrect image size")
    sys.exit()
if raw_size - calc_size == 2:
    print(W, H, bits_per_pixel, comp_meth, 2)
    sys.exit()

print(W, H, bits_per_pixel, comp_meth, 0)
