def knapsack_rec(weights,values,capacity,n):
    if n==0 or capacity==0:
        return 0
    if weights[n-1]>capacity:
        return knapsack_rec(weights,values,capacity,n-1)
    else:
        return max(knapsack_rec(weights,values,capacity,n-1),values[n-1]+knapsack_rec(weights, values, capacity-weights[n-1],n-1))
def knapsack_tab(weights, values, capacity, n):
    dp=[[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, capacity+1):
            if weights[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],values[i-1],dp[i-1][j-weights[i-1]])
    return dp[n][capacity]
def optimized_knapsack(weights, values, capacity, n):
    prev=[0]*(capacity+1)
    curr=[0]*(capacity+1)
    for i in range(1,n+1):
        for j in range(1, capacity+1):
            if weights[i-1]>j:
                curr[j]=prev[j]
            else:
                curr[j]=max(prev[j],values[i-1]+prev[j-weights[i-1]])
        prev, curr=curr, prev
    return prev[capacity]

values=[1,4,5,7]
weights=[2,3,5,7]
n=len(weights)
capacity=10
print('Max Profit(Naive Recursive Approach):',knapsack_rec(weights,values,capacity,n))
print('Max Profit(Tabulation 2D):',knapsack_tab(weights,values,capacity,n))
print('Max Profit(Tabulation 1D):',optimized_knapsack(weights,values,capacity,n))