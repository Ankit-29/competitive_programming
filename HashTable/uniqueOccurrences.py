'''
Given an array of integers arr, write a function that returns true if and 
only if the number of occurrences of each value in the array is unique.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
             No two values have the same number of occurrences.

Input: arr = [1,2]
Output: false

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''
from typing import List
from collections import Counter
def uniqueOccurrences(arr: List[int]) -> bool:
    Hash = Counter()
    testHash = Counter()
    
    for x in arr:
        Hash[x] += 1

    for x in Hash.keys():
        if(testHash[Hash[x]]==1):return False
        testHash[Hash[x]] = 1

    return True

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))
