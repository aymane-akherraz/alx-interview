#!/usr/bin/python3
""" Lockboxes Interview Challenge """


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened """
    opened_boxes = set()
    opened_boxes.add(0)
    bx_len = len(boxes)
    for i in range(bx_len):
        if i in opened_boxes:
            for j in boxes[i]:
                if j < bx_len:
                    opened_boxes.add(j)
        else:
            b = False
            for k in opened_boxes:
                if i in boxes[k]:
                    b = True
                    opened_boxes.add(i)
                    break
            if not b:
                return False
            else:
                continue

    return len(opened_boxes) == bx_len
