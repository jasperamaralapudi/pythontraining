def naive_rodcutting(p,n):
    if n==0:
        return n
    maxrevenue=float('-inf')
    for i in range(1,n+1):
        revenue=p[i-1]+naive_rodcutting(p,n-i)
        maxrevenue=max(maxrevenue, revenue)
    return maxrevenue
def memoized_rodcutting(p,n,memo={}):
    if n==0:
        return n
    if n in memo:
        return memo[n]
    maxrevenue=float('-inf')
    for i in range(1,n+1):
        revenue=p[i-1]+memoized_rodcutting(p,n-i,memo)
        maxrevenue=max(maxrevenue,revenue)
    memo[n]=maxrevenue
    return maxrevenue
def tabulated_rodcutting(p,n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        maxrevenue=float('-inf')
        for j in range(1,i+1):
            revenue=p[j-1]+dp[i-j]
            maxrevenue=max(maxrevenue,revenue)
        dp[i]=maxrevenue
    return dp[n]
def optimized_rodcutting(p,n):
    prev=[0]*(n+1)
    for i in range(1,n+1):
        maxrevenue=float('-inf')
        for j in range(1, min(i,len(p))+1):
            revenue=p[j-1]+prev[i-j]
            maxrevenue=max(maxrevenue,revenue)
        prev[i]=maxrevenue
    return prev[n]
p=[1,5,8,9]
n=4
print('Naive Recursive Approach:',naive_rodcutting(p,n))
print('Memoized Approach:',memoized_rodcutting(p,n))
print('Tabulated Approach:',tabulated_rodcutting(p,n))
print('Space-Optimized Approach:',optimized_rodcutting(p,n))