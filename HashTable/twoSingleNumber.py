'''
Given an array of numbers nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that 
appear only once.
Input:  [1,2,1,3,2,5]
Output: [3,5]
'''
from typing import List
def singleNumber(nums: List[int]) -> List[int]:
        ret = list()
        Hash = dict()
        count = 0
        
        for x in nums:
            Hash[x] = Hash[x]+1 if(x in Hash) else 1

        for x in Hash.keys():
            if(Hash[x]==1):
                ret.append(x)
                count += 1
                if(count==2):return ret

nums = [1,2,1,3,2,5]
print(singleNumber(nums))