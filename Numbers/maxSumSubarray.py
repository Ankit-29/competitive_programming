# Maximum Sum Subarray
# Kadane's algorithm
# Time Complexity O(n)

def maxSumSubarray(arr):
    currMax = 0 
    currSum = 0
    for x in range(len(arr)):
        currSum = max(0,currSum + arr[x])
        currMax = max(currMax,currSum)
    return currMax

arr = [1,-3,2,-5,7,6,-1,-4,11,-23]
print(maxSumSubarray(arr))
# 19





