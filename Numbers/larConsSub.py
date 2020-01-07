# Length of the largest subarray with contiguous elements
# TimeComplexity O(N^2)

def largestConsecutiveSubArray(arr):
    currMaxLen = 0
    for x in range(len(arr)):
        maxEle = arr[x]
        minEle = arr[x]
        for y in range(x+1,len(arr)):
            maxEle = max(maxEle,arr[y])
            minEle = min(minEle,arr[y])
            if((maxEle-minEle) == (y-x)):
                currMaxLen = max(currMaxLen,(y-x+1))
    return currMaxLen

arr = [2, 0, 2, 1, 4, 3, 1, 0]
print(largestConsecutiveSubArray(arr))