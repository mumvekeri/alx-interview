def canUnlockAll(boxes):
    # Initialize a set to keep track of unlocked boxes
    unlocked = set()
    unlocked.add(0)
    # Initialize a list to process keys
    keys = []
    keys.extend(boxes[0])
    
    # Process keys to unlock boxes
    while keys:
        new_key = keys.pop()
        if new_key not in unlocked and new_key < len(boxes):
            unlocked.add(new_key)
            keys.extend(boxes[new_key])
    
    # If the number of unlocked boxes equals the number of boxes, return True
    return len(unlocked) == len(boxes)
