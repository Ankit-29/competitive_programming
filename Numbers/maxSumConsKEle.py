# Maximum Sum of K Consecutive Elements
# Sliding Window Technique
# Time Complexity O(N)

def maxSumSubarrayOfSizeK(arr,k):
    currSum = 0
    maxSum = 0
    if(k<len(arr)): 
        return -1

    for x in range(k):
        currSum += arr[x]

    for x in range(k,len(arr)):
        currSum += arr[x]-arr[x-k]
        maxSum = max(currSum,maxSum)

    return maxSum

arr = [1,-3,2,-5,7,6,-1,-4,11,-23]
k = 3
print(maxSumSubarrayOfSizeK(arr,k))
