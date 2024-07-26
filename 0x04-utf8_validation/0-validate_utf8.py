#!/usr/bin/python3
""" alx-interview validate_utf8 challenge """


def validUTF8(data):
    """ Determines if a given data set
        represents a valid UTF-8 encoding
    """
    n_bytes = 0
    for byte in data:
        if n_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif(byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1
    return n_bytes == 0
