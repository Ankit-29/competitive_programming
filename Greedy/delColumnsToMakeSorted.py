'''
We are given an array A of N lowercase letter strings, all of the same length.
Now, we may choose any set of deletion indices, and for each string, we delete 
all the characters in those indices. e.g. if we have an array A = ["abcdef","uvwxyz"] 
and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], 
and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].
Suppose we chose a set of deletion indices D such that after deletions, each remaining 
column in A is in non-decreasing sorted order.Return the minimum possible value of D.length.
Example 1:
Input: ["cba","daf","ghi"]
Output: 1
Explanation: After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in 
             non-decreasing sorted order.
Input: ["a","b"]
Output: 0
'''
from typing import List
def minDeletionSize(A: List[str]) -> int:
    totalDel = 0
    l = len(A)
    for x in range(len(A[0])):
        last = A[0][x]
        for y in range(1,l):
            if(last>A[y][x]):
                totalDel += 1
                break
            last = A[y][x]
        
    
    
    return totalDel

A = ["cba","daf","ghi"]
print(minDeletionSize(A))