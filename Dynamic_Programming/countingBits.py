'''
Given a non negative integer number num. For every numbers i in the 
range 0 ≤ i ≤ num calculate the number of 1's in their binary 
representation and return them as an array.
Input: 2
Output: [0,1,1]

Input: 5
Output: [0,1,1,2,1,2]
'''
from typing import List
def countBits(num: int) -> List[int]:
    dp = [0]*(num+1)
    for x in range(1,num+1):
        if(x & 1):
            dp[x] = dp[x>>1]+1
        else:
            dp[x] = dp[x>>1]
    return dp

num = 5
print(countBits(num))