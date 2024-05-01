def canUnlockAll(boxes):
    if not boxes:
        return False
    
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]  # Start BFS from box 0

    while queue:
        current_box = queue.pop(0)  # Get the front of the queue
        keys = boxes[current_box]    # Keys in the current box

        for key in keys:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes are visited
    return all(visited)

# Example usage
boxes = [
    [1],        # Box 0 has key to Box 1
    [2],        # Box 1 has key to Box 2
    [3],        # Box 2 has key to Box 3
    [],         # Box 3 has no keys
]
print(canUnlockAll(boxes))  # Output: True

boxes_with_unreachable = [
    [1, 2],     # Box 0 has keys to Box 1 and Box 2
    [3],        # Box 1 has key to Box 3
    [],         # Box 2 has no keys
    [0],        # Box 3 has key back to Box 0 (cyclic, but cannot reach all)
]
print(canUnlockAll(boxes_with_unreachable))  # Output: False

