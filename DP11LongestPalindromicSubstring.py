def rec_lps(s):
    def ispalindrome(s):
        return s==s[::-1]
    def recurse(s):
        if len(s)<=1:
            return s
        maxlen=0
        maxsubsequence=''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                subseq=s[i:j]
                if ispalindrome(subseq) and len(subseq)>maxlen:
                    maxlen=len(subseq)
                    maxsubseq=subseq
        return maxsubseq
    return recurse(s)
def memoized_lps(s):
    memo = {} 

    def is_palindrome(sub):
        return sub == sub[::-1]

    def recurse(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j:
            return s[i]
        if is_palindrome(s[i:j+1]):
            memo[(i, j)] = s[i:j+1]
            return s[i:j+1]
        
        maxsubseq = ''
        for k in range(i, j):
            left = recurse(i, k)
            right = recurse(k+1, j)
            if len(left) > len(maxsubseq):
                maxsubseq = left
            if len(right) > len(maxsubseq):
                maxsubseq = right
        
        memo[(i, j)] = maxsubseq
        return maxsubseq

    return recurse(0, len(s) - 1)

def tabulated_lps(s):
    n=len(s)
    dp=[['' for _  in range(n)]for _ in range(n)]
    for i in range(n):
        dp[i][i]=s[i]
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            if s[i]==s[j] and length==2:
                dp[i][j]=s[i]+s[j]
            elif s[i]==s[j]:
                dp[i][j]=s[i]+dp[i+1][j-1]+s[j]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j-1],key=len)
    return dp[0][n-1]
s='banana'
print('Longest Palindromic Substring(Naive Recursive Approach):',rec_lps(s))
print('Longest Palindromic Substring(Memoized Approach):',memoized_lps(s))
print('Longest Palindromic Substring(Tabulated Approach):',tabulated_lps(s))