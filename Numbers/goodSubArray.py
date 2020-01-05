# You are given N elements, a1,a2,a3….aN. Find the number of good sub-arrays.
# A good sub-array is a sub-array [ai,ai+1,ai+2….aj] such that (ai+ai+1+ai+2+….+aj) 
# is divisible by N.

# Application of PigeonHole Principle
# TimeComplexity O(n)

def totalGoodSubArray(arr,n):
    prefixSumMod = [0]*n
    prefixSumMod[0] = 1
    sumVal = 0
    res = 0
    for x in range(len(arr)):
        sumVal += arr[x]
        prefixSumMod[sumVal%n] += 1
        
    for x in prefixSumMod:
        res += (x*(x-1))/2  

    return res

n = 5
arr = [5,2,8,6,9]
print(totalGoodSubArray(arr,n))