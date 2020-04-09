'''
Given a list of daily temperatures T,return a list such that,for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is 
no future day for which this is possible, put 0 instead.
For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your 
output should be [1, 1, 4, 2, 1, 1, 0, 0].
Note: The length of temperatures will be in the range [1, 30000]. Each temperature will 
be an integer in the range [30, 100].
'''

from typing import List
def dailyTemperatures(T: List[int]) -> List[int]:
    Hash = dict()
    l = len(T)
    for x in range(l-1,-1,-1):
        MIN = 30001
        for y in range(T[x]+1,101):
            if(y in Hash and Hash[y]<MIN):
                MIN = Hash[y]  
        
        Hash[T[x]] = x
        
        T[x] = 0 if MIN==30001 else MIN-x
            
    return T

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))