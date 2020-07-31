#!/usr/bin/python
import base64
import binascii

h = binascii.hexlify
b = base64.b64encode


def enc(f):
    e = b(f)
    print(" e : %s" % e)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    c = h(bytearray(z))
    return c

print(enc('10110100'))
