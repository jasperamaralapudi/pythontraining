def rec_is_interleave(s1, s2, s3):
  def recurse(i, j, k):
    if k == len(s3):
      return i == len(s1) and j == len(s2)
    if i < len(s1) and s1[i] == s3[k]:
      if recurse(i+1, j, k+1):
        return True
    if j < len(s2) and s2[j] == s3[k]:
      if recurse(i, j+1, k+1):
        return True
    return False

  return recurse(0, 0, 0)
def memoized_is_interleave(s1, s2, s3):
  memo = {}

  def recurse(i, j, k):
    if (i, j, k) in memo:
      return memo[(i, j, k)]
    if k == len(s3):
      return i == len(s1) and j == len(s2)
    if i < len(s1) and s1[i] == s3[k]:
      if recurse(i+1, j, k+1):
        memo[(i, j, k)] = True
        return True
    if j < len(s2) and s2[j] == s3[k]:
      if recurse(i, j+1, k+1):
        memo[(i, j, k)] = True
        return True
    memo[(i, j, k)] = False
    return False

  return recurse(0, 0, 0)
def tabulated_is_interleave(s1, s2, s3):
  m, n, k = len(s1), len(s2), len(s3)
  dp = [[[False for _ in range(k+1)] for _ in range(n+1)] for _ in range(m+1)]

  for i in range(m+1):
    for j in range(n+1):
      dp[i][j][0] = True

  for i in range(1, m+1):
    for k in range(1, k+1):
      dp[i][0][k] = dp[i-1][0][k-1] and s1[i-1] == s3[k-1]

  for j in range(1, n+1):
    for k in range(1, k+1):
      dp[0][j][k] = dp[0][j-1][k-1] and s2[j-1] == s3[k-1]

  for i in range(1, m+1):
    for j in range(1, n+1):
      for k in range(1, k+1):
        dp[i][j][k] = (dp[i-1][j][k-1] and s1[i-1] == s3[k-1]) or (dp[i][j-1][k-1] and s2[j-1] == s3[k-1])

  return dp[m][n][k]
def optimized_is_interleave(s1, s2, s3):
  m, n, k = len(s1), len(s2), len(s3)
  if m + n != k:
    return False

  prev = [False] * (n+1)
  curr = [False] * (n+1)

  for j in range(n+1):
    prev[j] = True

  for i in range(1, m+1):
      curr[0] = False
      for j in range(1, n+1):
          curr[j] = (curr[j-1] and s2[j-1] == s3[i+j-1]) or (prev[j] and s1[i-1] == s3[i+j-1])
  prev, curr = curr, prev

  return prev[-1]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print("Is s3 an interleaving of s1 and s2?(Naive Recursive Approach):", rec_is_interleave(s1, s2, s3))
print("Is s3 an interleaving of s1 and s2?(Memoized Approach):", memoized_is_interleave(s1, s2, s3))
print("Is s3 an interleaving of s1 and s2?(Tabulated Approach):", tabulated_is_interleave(s1, s2, s3))
print("Is s3 an interleaving of s1 and s2?(Optimized Approach):", optimized_is_interleave(s1, s2, s3))