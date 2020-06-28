'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
from typing import List

class NumArray:
     
    def __init__(self, nums: List[int]):
        self.dp = [0]*len(nums)
        if(len(nums)):self.dp[0] = nums[0]
        for x in range(1,len(nums)):
            self.dp[x] = nums[x] + self.dp[x-1]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i-1] if i!=0 else self.dp[j] 


nums = [-2,0,3,-5,2,-1]
ranges = [[0,2],[2,5],[0,5]]

obj = NumArray(nums)
for r in ranges:
    print(obj.sumRange(r[0],r[1]))


