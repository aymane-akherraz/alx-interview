#!/usr/bin/python3
""" alx-interview validate_utf8 challenge """


def validUTF8(data):
    """ Determines if a given data set
        represents a valid UTF-8 encoding
    """

    if not data:
        return False

    i = 0
    length = len(data)

    while i < length:
        byte = data[i]
        if byte < 128:
            i += 1
        elif byte >= 192 and byte < 224:
            if i + 1 < length and 128 <= data[i + 1] < 192:
                i += 2
            else:
                return False
        elif byte >= 224 and byte < 240:
            if (i + 2 < length and 128 <= data[i + 1] < 192
                    and 128 <= data[i + 2] < 192):
                i += 3
            else:
                return False
        elif byte >= 240 and byte < 248:
            if (i + 3 < length and 128 <= data[i + 1] < 192
                    and 128 <= data[i + 2] < 192 and 128 <= data[i + 3] < 192):
                i += 4
            else:
                return False
        else:
            return False
    return True
