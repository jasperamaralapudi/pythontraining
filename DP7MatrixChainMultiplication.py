def rec_mco(p, i, j):
    if i == j:
        return 0
    min_cost = float('inf')
    for k in range(i, j):
        cost = rec_mco(p, i, k) + rec_mco(p, k + 1, j) + p[i - 1] * p[k] * p[j]
        min_cost = min(min_cost, cost)
    return min_cost

def dp_mco(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # L is the chain length.
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][n]

# Optimized version using memoization with lru_cache.
from functools import lru_cache

def optimized_mco(p):
    n = len(p) - 1
    
    @lru_cache(maxsize=None)
    def compute(i, j):
        if i == j:
            return 0
        min_cost = float('inf')
        for k in range(i, j):
            cost = compute(i, k) + compute(k + 1, j) + p[i - 1] * p[k] * p[j]
            min_cost = min(min_cost, cost)
        return min_cost
    
    return compute(1, n)

p = [30, 35, 15, 5, 10]

print("Recursive MCO:", rec_mco(p, 1, len(p) - 1))
print("DP MCO:", dp_mco(p))
print("Optimized MCO (Memoized):", optimized_mco(p))
