def rec_eggdrop(n,k):
    if k==0 or k==1:
        return k
    if n==1:
        return k
    minattempts=float('inf')
    for i in range(1,k+1):
        attempts=1+max(rec_eggdrop(n-1,i-1),rec_eggdrop(n,k-i))
        minattempts=min(minattempts,attempts)
    return minattempts
def memoized_eggdrop(n,k,memo={}):
    if (n,k) in memo:
        return memo[(n,k)]
    if k==0 or k==1:
        return k
    minattempts=float('inf')
    for i in range(1,k+1):
        attempts=1+max(memoized_eggdrop(n-1,i-1,memo),memoized_eggdrop(n,k-i,memo))
        minattempts=min(minattempts,attempts)
    memo[(n,k)]=minattempts
    return minattempts
def tabulated_eggdrop(n,k):
    dp=[[0 for _ in range(k+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        dp[i][0]=0
        dp[i][1]=1
    for j in range(1,k+1):
        dp[1][j]=j
    for i in range(2,n+1):
        for j in range(2,k+1):
            minattempts=float('inf')
            for x in range(1,j+1):
                attempts=1+max(dp[i-1][x-1],dp[i][j-x])
                minattempts=min(minattempts, attempts)
            dp[i][j]=minattempts
    return dp[n][k]
n=2
k=10
print('Naive Recursive Approach:',rec_eggdrop(n,k))
print('Memoized Approach:',memoized_eggdrop(n,k))
print('Tabulated Approach:',tabulated_eggdrop(n,k))