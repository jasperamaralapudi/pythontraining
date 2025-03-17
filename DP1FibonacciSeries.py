def fib_rec(n):
    if n<=1:
        return n
    return fib_rec(n-1)+fib_rec(n-2)
def fib_tab(n):
    dp=[0]*(n+1)
    if n<=1:
        return n
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
def fib_memo(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=1:
        return n
    memo[n]=fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
fibrec=[fib_rec(n) for n in range(7)]
fi=[fib_memo(n) for n in range(7)]
fibtab=[fib_tab(n) for n in range(7)]
print('Fibonacci Series (Naive Recursion): ',fibrec)
print('Fibonacci Series (Tabulation): ',fibtab)
print('Fibonacci Series (Memoization): ',fi)