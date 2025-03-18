def rec_subsetsum(s,t,n):
    if t==0:
        return True
    if n==0 and t!=0:
        return False
    if s[n-1]>t:
        return rec_subsetsum(s,t,n-1)
    return rec_subsetsum(s,t-s[n-1],n-1) or rec_subsetsum(s,t,n-1)
def memoized_subsetsum(s,t,n,memo={}):
    if (t,n) in memo:
        return memo[(t,n)]
    if t==0:
        return True
    if n==0 and t!=0:
        return False
    if s[n-1]>t:
        res=memoized_subsetsum(s,t,n-1,memo)
    else:
        res=memoized_subsetsum(s,t-s[n-1],n-1) or memoized_subsetsum(s,t,n-1)
    memo[(t,n)]=res
    return res
def tabulated_subsetsum(s,t,n):
    dp=[[False for _ in range(t+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,t+1):
            if s[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-s[i-1]]
    return dp[n][t]
def optimized_subsetsum(s,t,n):
    dp=[False for _ in range(t+1)]
    dp[0]=True
    for i in range(1,n+1):
        for j in range(t,s[i-1]-1,-1):
            dp[j]=dp[j] or dp[j-s[i-1]]
    return dp[t]
s=[3,34,4,12,5,2]
t=9
n=len(s)
print('Naive Recursive Approach:',rec_subsetsum(s,t,n))
print('Memoized Approach:',memoized_subsetsum(s,t,n))
print('Tabulated Approach:',tabulated_subsetsum(s,t,n))
print('Space-Optimized Approach:',optimized_subsetsum(s,t,n))