'''
Apple Orchard
Allie has bought a new apple orchard. The orchard has a single file of trees, number
from 1 to N. Each tree has a certain number of ripe apples.
Allie has a rule she wants to follow. She wants to pluck an equal amount of apples fro
each tree from which she collects apples.
Allie can start collecting apples from any tree, but once she starts collecting, she coll
from every consecutive tree until she reaches the last tree she wants to collect from.
the maximum number of apples she can fetch from the orchard.
Input Specification:
An array of N elements (a1,a2 a3......AN], denoting the number of ripe
apples in each tree of the orchard.

Input: [80,48,82]
​Output: 144

Input: [8,40,77]
Output: 80
'''

from typing import List


def maxApple(arr: List[int]) -> int:
    m = 0
    for x in range(0,len(arr)):
        left = x-1; right = x
        tot = 0; canCollect = True
        while(canCollect):
            canCollect = False
            if left>=0 and arr[left] >= arr[x]:
                tot += arr[x]
                canCollect = True
                left -= 1
            
            if right>=0 and right<len(arr) and arr[right]>=arr[x]:
                tot += arr[x]
                canCollect = True
                right += 1

        m = max(m,tot)
    return m


arr = [80,48,82]
print(maxApple(arr))

