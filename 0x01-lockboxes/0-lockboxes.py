#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

    Args:
        boxes (list of list): The list of boxes where each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''

    n = len(boxes)

    opened_boxes = set()

    stack = [0]

    while stack:
        box_index = stack.pop()
        opened_boxes.add(box_index)

        for key in boxes[box_index]:
            if key < n and key not in opened_boxes:
                stack.append(key)

    return len(opened_boxes) == n

