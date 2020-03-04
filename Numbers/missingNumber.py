'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Input: [3,0,1]
Output: 2
'''

from typing import List
def missingNumber(nums: List[int]) -> int:
    l = len(nums)
    actual = 0 
    total = ((l)*(l+1))//2
    for x in nums:
        actual += x
    
    return total - actual

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))