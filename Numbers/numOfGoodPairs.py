'''
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

'''
from typing import List
def numIdenticalPairs(nums: List[int]) -> int:
    Hash = {}
    ret = 0
    for x in nums:
        if(x in Hash):
            Hash[x] +=1
        else:
            Hash[x] = 1
    
    for key in Hash.keys():
        if(Hash[key]>1):
            ret += (Hash[key]*(Hash[key]-1))//2
    
    return ret

nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))