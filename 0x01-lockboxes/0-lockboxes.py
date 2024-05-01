#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]
    
    while keys:
        new_keys = []
        for key in keys:
            if unlocked[key] == False:
                unlocked[key] = True
            for new_key in boxes[key]:
                if new_key < len(boxes) and not unlocked[new_key]:
                    new_keys.append(new_key)
        keys = new_keys
    
    return all(unlocked)

# Example of usage:
# print(canUnlockAll([[1], [2], [3], [4], []])) # Returns True
# print(canUnlockAll([[1, 2], [2, 3], [3], []])) # Returns False
