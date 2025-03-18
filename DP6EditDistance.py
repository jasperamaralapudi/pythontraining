def rec_edit_distance(str1,str2):
    if len(str1)==0:
        return len(str2)
    if len(str2)==0:
        return len(str1)
    if str1[0]==str2[0]:
        return rec_edit_distance(str1[1:],str2[1:])
    else:
        return 1+min(rec_edit_distance(str1,str2[1:]),rec_edit_distance(str1[1:],str2),rec_edit_distance(str1[1:],str2[1:]))
def tab_edit_distance(str1,str2):
    m,n=len(str1),len(str2)
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return dp[m][n]
def optimized_edit_distance(str1,str2):
    m,n=len(str1),len(str2)
    prev=[0]*(n+1)
    curr=[0]*(n+1)
    for j in range(n+1):
        prev[j]=j
    for i in range(1,m+1):
        curr[0]=i
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                curr[j]=prev[j-1]
            else:
                curr[j]=1+min(prev[j],curr[j-1],prev[j-1])
        prev,curr=curr,prev
    return prev[n]
str1='kitten'
str2='sitting'
print('Edit Distance(Naive Recursive Approach):',rec_edit_distance(str1,str2))
print('Edit Distance(DP Tabulation Approach 2D):',tab_edit_distance(str1,str2))
print('Edit Distance(Optimized Approach 1D):',optimized_edit_distance(str1,str2))