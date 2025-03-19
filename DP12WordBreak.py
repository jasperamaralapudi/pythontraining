def rec_wordbreak(s,word_dict):
    def recurse(s):
        if not s:
            return True
        for word in word_dict:
            if s.startswith(word):
                if recurse(s[len(word):]):
                    return True
        return False
    return recurse(s)
def memoized_wordbreak(s,word_dict):
    memo={}
    def recurse(s):
        if s in memo:
            return memo[s]
        if not s:
            return True
        for word in word_dict:
            if s.startswith(word):
                if recurse(s[len(word):]):
                    memo[s]=True
                    return True
        memo[s]=False
        return False
    return recurse(s)
def tabulated_wordbreak(s,word_dict):
    dp=[False]*(len(s)+1)
    dp[0]=True
    for i in range(1,len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i]=True
                break
    return dp[-1]
s='leetcode'
word_dict={'leet','code'}
print('Naive Recursive Approach:',rec_wordbreak(s,word_dict))
print('Memoized Approach:',memoized_wordbreak(s,word_dict))
print('Tabulated Approach:',tabulated_wordbreak(s,word_dict))