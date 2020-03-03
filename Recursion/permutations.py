'''
Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from typing import List
def generatePerms(nums: List[int],left: int,right: int,ret: List[int])->List[int]:
    if(left==right):
        ret.append(nums[::])
    else:
        for x in range(left,right):
            nums[x],nums[left] = nums[left],nums[x]
            generatePerms(nums,left+1,right,ret)
            nums[x],nums[left] = nums[left],nums[x]
    return ret

nums = [1,2,3]
print(generatePerms(nums,0,len(nums),list()))