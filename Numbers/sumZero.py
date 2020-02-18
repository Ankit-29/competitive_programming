'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
Input: n = 5
Output: [-7,-1,1,3,4]
Any Possible combination is accepted e.g. [-5,-1,1,2,3] , [-3,-1,2,-2,4].
'''
from typing import List
def sumZero(n: int) -> List[int]:
    ret = list()
    if(n & 1):
        ret.append(0)
        n -= 1
    
    while(n):
        ret.append(n)
        ret.append(-n)
        n -=2
        
    return ret

n = 5
print(sumZero(n))
# [0, 4, -4, 2, -2]
