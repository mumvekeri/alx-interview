#!/usr/bin/python3

def canUnlockAll(boxes):
    length = len(boxes)
    keys = set()
    opened_boxes = set()
    stack = [0]

    while stack:
        box_index = stack.pop()
        opened_boxes.add(box_index)
        keys.update(boxes[box_index])
        
        for key in keys:
            if key < length and key not in opened_boxes:
                stack.append(key)

    return len(opened_boxes) == length

