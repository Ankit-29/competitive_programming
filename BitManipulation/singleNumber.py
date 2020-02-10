'''
Given a non-empty array of integers, every element appears twice 
except for one. Find that single one.
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
'''
def singleNumber(nums: int) -> int:
    ans = 0
    for x in nums:
        ans ^= x
    
    return ans
    
nums = [4,1,2,1,2]
print(singleNumber(nums))