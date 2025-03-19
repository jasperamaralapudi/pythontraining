def rec_decodings(s):
    def recurse(i):
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        count=recurse(i+1)
        if i+1<len(s) and '10'<=s[i:i+2]<='26':
            count+=recurse(i+2)
        return count
    return recurse(0)
def memoized_decodings(s):
    memo={}
    def recurse(i):
        if i in memo:
            return memo[i]
        if i==len(s):
            return 1
        if s[i]=='0':
            return 0
        count=recurse(i+1)
        if i+1<len(s) and '10'<=s[i:i+2]<='26':
            count+=recurse(i+2)
        memo[i]=count
        return count
    return recurse(0)
def tabulated_decodings(s):
    n=len(s)
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        if s[i-1]!='0':
            dp[i]+=dp[i-1]
        if i>=2 and '10'<=s[i-2:i]<='26':
            dp[i]+=dp[i-2]
    return dp[n]
def optimized_decodings(s):
    if s[0]=='0':
        return 0
    n=len(s)
    prev,curr=1,1
    for i in range(1,n):
        temp=curr
        if s[i]=='0':
            curr=0
        if '10'<=s[i-1:i+1]<='26':
            curr+=prev
        prev=temp
    return curr
s='226'
print('Naive Recursive Approach:',rec_decodings(s))
print('Memoized Approach:',memoized_decodings(s))
print('Tabulated Approach:',tabulated_decodings(s))
print('Optimized Approach:',optimized_decodings(s))