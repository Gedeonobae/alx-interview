#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """method"""
    nbytes = 0

    byte1 = 1 << 7
    byte2 = 1 << 6

    for i in data:
        m = 1 << 7
        if nbytes == 0:
            while m & i:
                nbytes += 1
                m = m >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (i & byte1 and not (i & byte2)):
                return False
        nbytes -= 1
    return nbytes == 0
