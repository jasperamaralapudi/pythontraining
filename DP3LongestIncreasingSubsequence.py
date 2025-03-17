def lis_rec(arr):
    if len(arr)==0:
        return 0
    max_len=1
    for i in range(1,len(arr)):
        if arr[i]>arr[0]:
            max_len=max(max_len, 1 + lis_rec(arr[1:]))
    return max_len
def lis_tab(arr):
    n=len(arr)
    dp=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
def lis_mem(arr,memo={}):
    if len(arr):
        return 0
    if tuple(arr) in memo:
        return memo[tuple(arr)]
    max_len=1
    for i in range(1, len(arr)):
        if arr[i]>arr[0]:
            max_len=max(max_len,1+lis_mem(arr[1:],memo))
    memo[tuple(arr)]=max_len
    return max_len
arr=[10,22,9,33,21,50,41,60,80]
print('Naive Recursive Approach:',lis_rec(arr))
print('LIS(Tabulation Approach):',lis_tab(arr))
print('LIS(Memoization Approach):',lis_tab(arr))