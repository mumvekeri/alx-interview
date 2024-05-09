def minOperations(n):
    if n <= 1:
        return 0
    
    # Initialize dp array with a large number (inf) and dp[1] = 0
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        # Find all factors of i
        j = 1
        while j * j <= i:
            if i % j == 0:
                # Factor pair (j, i // j)
                dp[i] = min(dp[i], dp[j] + (i // j))
                if i // j != i:
                    dp[i] = min(dp[i], dp[i // j] + j)
            j += 1
    
    return dp[n] if dp[n] != float('inf') else 0

# Test the function
n = 9
print(minOperations(n))  # Output: 6

