#!/usr/bin/env python3

import hid
import binascii
import random
import time
import colorsys
import numpy as np

h = hid.enumerate()

#print(h)

my_idx = None
for j in range(len(h)):
#    print(h[j])
    if((h[j]['interface_number'] == 2) & (h[j]['product_string'] == 'N-KEY Device')):
        my_idx = j

#print(h[my_idx]['path'])

d = hid.Device(path=h[my_idx]['path'])

#commandstr_rainbow = binascii.unhexlify('5db30003000000f50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#commandstr_breathe = binascii.unhexlify('5db30001ff0000f5000100ff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#commandstr2 = binascii.unhexlify('5db50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#commandstr3 = binascii.unhexlify('5db40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
#commandstr4 = binascii.unhexlify('5db50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')

#d.write(commandstr_rainbow)
#d.write(commandstr2)
#d.write(commandstr3)
#d.write(commandstr4)

d.write(binascii.unhexlify('5dbc0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#d.write(binascii.unhexlify('5dbc000101010010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101011010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101012010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101013010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101014010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101015010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101016010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101017010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101018010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc000101019010007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))
#d.write(binascii.unhexlify('5dbc00010101a008007500f26900ec5f00e55400df4b00d94b00d94b00d94b00d94b00d94b00d94e00db5800e16200e86d00ee7900f58500fb00000000000000'))

#top row starts at 02
d.write(binascii.unhexlify('5dbc00010101021000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#esc is 0x15, 0x16 is not anything
d.write(binascii.unhexlify('5dbc00010101151000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#` is 0x2a
d.write(binascii.unhexlify('5dbc000101012a1000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#0x30 is 6, 0x40 is q, 0x3f is tab
d.write(binascii.unhexlify('5dbc000101013f1000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#0x50 is nothing, so is 0x52, ox54 is capslock, a write of 0x10 lights does not clear pgdn
d.write(binascii.unhexlify('5dbc00010101541000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#0x64 is pgdn, 0x6b is z, 0x69 is shift, 0x6a is nothing
d.write(binascii.unhexlify('5dbc00010101691000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#0x70 is n, 0x76 is left of rtshift, 0x78 is right of rshift, 0x69 is end, 0x7e is left-ctrl
d.write(binascii.unhexlify('5dbc000101017e1000ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))
#0x80 is win key, 0x88 is prtscr, 0x8a is nothing, 0x8e is right fn, 0xa0 is dn, 0xa1 is rt
d.write(binascii.unhexlify('5dbc00010101a10400ffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'))

#leftmost border keys:
#0x02 is voldn (probably really 0x00 but nothing is here physically
#0x15 is esc
#0x2a is `
#0x3f is tab
#0x54 is capslock
#0x69 is leftshift
#0x7e is leftctrl
#0x93 is leftmost of arrowkey row at bottom

d.nonblocking = 1
lasthue = 0.0
huearray = np.zeros(21)

while(True):
    for j in range(20):
        huearray[20-j] = huearray[19-j]
    huearray[0] += (random.random()-0.45)/10.0
    #huearray[0] += 0.03
    if(huearray[0] < 0.0):
        huearray[0] += 1.0
    if(huearray[0] >= 1.0):
        huearray[0] -= 1.0
    for j in range(8):
        basestr = '5dbc00010101'
        rangestr = '%02x'%(j*21)
        valstr = ''
        for k in range(16):
            (r, g, b) = colorsys.hsv_to_rgb(huearray[k], 1.0, 1.0)
            valstr = valstr + '%02x'%int(r*255.0) + '%02x'%int(g*255.0) + '%02x'%int(b*255.0)
        d.write(binascii.unhexlify(basestr + rangestr + '1000' + valstr))
        basestr = '5dbc00010101'
        rangestr = '%02x'%((j*21)+16)
        valstr = ''
        for k in range(5):
            (r, g, b) = colorsys.hsv_to_rgb(huearray[k+16], 1.0, 1.0)
            valstr = valstr + '%02x'%int(r*255.0) + '%02x'%int(g*255.0) + '%02x'%int(b*255.0)
        d.write(binascii.unhexlify(basestr + rangestr + '0300' + valstr))
    time.sleep(0.05)
        
while(False):
    for j in range(10):
        basestr = '5dbc00010101'
        rangestr = '%02x'%(j*16)
        valstr = ''
        for k in range(16):
            lasthue += (random.random()-0.49)/80.0
            if(lasthue < 0.0):
                lasthue += 1.0
            if(lasthue > 1.0):
                lasthue -= 1.0
            (r,g,b) = colorsys.hsv_to_rgb(lasthue,1.0,1.0)
            valstr = valstr + '%02x'%int(r*255.0) + '%02x'%int(g*255.0) + '%02x'%int(b*255.0)
        #print(basestr + rangestr + '1000' + valstr)
        d.write(binascii.unhexlify(basestr + rangestr + '1000' + valstr))
    basestr = '5dbc00010101'
    rangestr = 'a0'
    valstr = ''
    for k in range(8):
        lasthue += (random.random()-0.49)/80.0
        if(lasthue < 0.0):
            lasthue += 1.0
        if(lasthue > 1.0):
            lasthue -= 1.0
        (r,g,b) = colorsys.hsv_to_rgb(lasthue,1.0,1.0)
        valstr = valstr + '%02x'%int(r*255.0) + '%02x'%int(g*255.0) + '%02x'%int(b*255.0)
    d.write(binascii.unhexlify(basestr + rangestr + '0800' + valstr))
    time.sleep(0.05)
