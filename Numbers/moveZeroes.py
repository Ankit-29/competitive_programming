'''
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
Note:
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

from typing import List

def moveZeroes(nums: List[int]) -> List[int]:
    lastZeroIdx = 0
    for x in range(len(nums)):
        if(nums[x]!=0):
            nums[lastZeroIdx] , nums[x] = nums[x],nums[lastZeroIdx]
            lastZeroIdx += 1
    
    return nums

nums =  [0,1,0,3,12]
print(moveZeroes(nums))