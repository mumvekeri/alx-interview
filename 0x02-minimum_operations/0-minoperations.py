#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    if n <= 1:
        return 0
    
    pasted_chars = 1  # Number of characters in the file
    clipboard = 0     # Number of 'H' characters copied
    counter = 0       # Operations counter
    
    while pasted_chars < n:
        if clipboard == 0:
            # Copy all
            clipboard = pasted_chars
            counter += 1

        if pasted_chars == 1:
            # Paste
            pasted_chars += clipboard
            counter += 1
            continue
        
        remaining = n - pasted_chars
        
        if remaining < clipboard:
            return 0
        
        if remaining % pasted_chars != 0:
            # Paste current clipboard
            pasted_chars += clipboard
            counter += 1
        else:
            # Copy all
            clipboard = pasted_chars
            # Paste
            pasted_chars += clipboard
            counter += 2
    
    if pasted_chars == n:
        return counter
    else:
        return 0

# Test the function
n = 9
print(minOperations(n))  # Output: 6

