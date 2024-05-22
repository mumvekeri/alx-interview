#!/usr/bin/env python3
"""UTF-8 MODULE
"""


def validUTF8(data):
    def check_following_bytes(start, count):
        for i in range(start + 1, start + count + 1):
            if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                return False
        return True
    
    i = 0
    while i < len(data):
        byte = data[i]
        if (byte & 0b10000000) == 0:
            i += 1
            continue
        elif (byte & 0b11100000) == 0b11000000:
            if not check_following_bytes(i, 1):
                return False
            i += 2
        elif (byte & 0b11110000) == 0b11100000:
            if not check_following_bytes(i, 2):
                return False
            i += 3
        elif (byte & 0b11111000) == 0b11110000:
            if not check_following_bytes(i, 3):
                return False
            i += 4
        else:
            return False
    return True
