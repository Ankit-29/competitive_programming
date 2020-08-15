'''
Given an array where every element occurs three times, except one element which occurs only once. 
Find the element that occurs once. Expected time complexity is O(n) and O(1) extra space.

Input: arr[] = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
Output: 2
In the given array all element appear three times except 2 which appears once.

Input: arr[] = [10, 20, 10, 30, 10, 30, 30]
Output: 20
In the given array all element appear three times except 20 which appears once.
'''

from typing import List


def findSingleOccurrence(arr: List[int]) -> int:
    res = 0
    for x in range(0, 32):
        tot = 0
        i = 1 << x
        for y in range(len(arr)):
            if(arr[y] & i):
                tot += 1
        if(tot % 3):
            res |= i

    return res


arr = [10, 20, 10, 30, 10, 30, 30]
print(findSingleOccurrence(arr))
