#!/usr/bin/python3
'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

    Args:
        boxes (list of list): The list of boxes where each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''

    # Total number of boxes
    n = len(boxes)

    # Set to keep track of opened boxes
    opened_boxes = set()

    # Stack to perform DFS (starting with box 0)
    stack = [0]

    while stack:
        box_index = stack.pop()
        opened_boxes.add(box_index)

        # Iterate through keys in the current box
        for key in boxes[box_index]:
            if key < n and key not in opened_boxes:
                stack.append(key)

    # Check if all boxes can be opened (i.e., all boxes are in the opened set)
    return len(opened_boxes) == n

