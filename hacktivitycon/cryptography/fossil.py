#!/usr/bin/python
import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = '37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'

test = "test"

def enc(f):
    e = b(f)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    c = h(bytearray(z))
    return c


def dec(f):
    c = binascii.unhexlify(bytearray(f))
    print(c)
    z = []
    i = 0
    while i < len(c):
        z += [ c[i] ]
        i = i + 1
    print(z)
    e = z.decode('base64')
    return e

print(dec(c))
