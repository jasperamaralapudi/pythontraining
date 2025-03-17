def naive_lcs(X, Y):
    if len(X)==0 or len(Y)==0:
        return 0
    if X[0]==Y[0]:
        return 1+naive_lcs(X[1:],Y[1:])
    else:
        return max(naive_lcs(X,Y[1:]),naive_lcs(X[1:],Y))
def lcs_dp(X,Y):
    m,n =len(X), len(Y)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
def lcs_optimized(X,Y):
    m,n=len(X),len(Y)
    prev=[0]*(n+1)
    curr=[0]*(n+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                curr[j]=1+curr[j-1]
            else:
                curr[j]=max(prev[j], curr[j-1])
        prev,curr=curr,prev
    return prev[n]
X="AGGTAB"
Y="GXTXAYB"
print("X=",X)
print("Y=",Y)
print('Naive Recursive Approach:',naive_lcs(X,Y))
print('DP Tabulation Approach (2D):',lcs_dp(X,Y))
print('Space Optimized Approach (1D):',lcs_optimized(X,Y))