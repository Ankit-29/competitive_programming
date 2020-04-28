'''
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.
Return the minimum size of the set so that at least half of the integers of the array are removed.
Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
'''

from typing import List
def minSetSize(arr: List[int]) -> int:
    Hash = {}
    l = len(arr)//2
    for x in arr:
        Hash[x] = 1 if x not in Hash else Hash[x] + 1
    
    sortedVals = sorted(Hash.values(),reverse=True)
    total = 0 
    for idx,val in enumerate(sortedVals):
        total += val  
        if(total>=l):
            return idx+1

arr = [3,3,3,3,5,5,5,2,2,7]
print(minSetSize(arr))
