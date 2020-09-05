'''
Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return True if you can make arr equal to target, or False otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [1,12], arr = [12,1]
Output: true
Example 4:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr doesn't have value 9 and it can never be converted to target.
Example 5:

Input: target = [1,1,1,1,1], arr = [1,1,1,1,1]
Output: true
'''

from typing import List


def canBeEqual(target: List[int], arr: List[int]) -> bool:
    if(len(target) > len(arr)):
        return False
    count = {}
    count2 = {}
    for x in target:
        if(x in count):
            count[x] += 1
        else:
            count[x] = 1

    for x in arr:
        if(x in count2):
            count2[x] += 1
        else:
            count2[x] = 1

    for x in count.keys():
        if(x not in count2):
            return False
        if(count[x] > count2[x]):
            return False

    return True


target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual(target,arr))