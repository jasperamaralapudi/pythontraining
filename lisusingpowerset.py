def isIncreasing(subset):
    for i in range(1, len(subset)):
        if subset[i] <= subset[i - 1]:
            return False
    return True

def lis(nums):
    n = len(nums)
    maxlen = 0

    for m in range(1, 1 << n):  
        subset = []
        for i in range(n):
            if m & (1 << i):
                subset.append(nums[i])
        if isIncreasing(subset):
            maxlen = max(maxlen, len(subset))

    return maxlen

nums = [10,9,2,5,3,7,101,18]
print(lis(nums))
