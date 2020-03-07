'''
You are a professional robber planning to rob houses along a street.Each house has 
a certain amount of money stashed, the only constraint stopping you from robbing each
of them is that adjacent houses have security system connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
Input: [2,7,9,3,1]
Output: 12
Input: [1,2,3,1]
Output: 4
Input: [2,1,1,2]
Output: 4
'''
from typing import List
def rob(nums: List[int]) -> int:
    l = len(nums)
    if(l<=0):return 0
    if(l<=2):return max(nums)
    best = 0; dp = [0]*(l)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[2]+nums[0]
    best = max(dp[0],dp[1],dp[2])

    for x in range(3,l):
        dp[x] = nums[x]+max(dp[x-2],dp[x-3])
        best = max(dp[x],best)
    
    return best

nums = [2,7,9,3,1]
print(rob(nums))
