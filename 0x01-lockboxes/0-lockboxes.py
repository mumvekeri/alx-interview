#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return True
    
    visited = [False] * n
    visited[0] = True
    stack = [0]
    
    while stack:
        box_index = stack.pop()
        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    
    return all(visited)
