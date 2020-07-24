'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    Hash = {}
    ret = []
    for x in nums:
        if(x in Hash):
            Hash[x] += 1
        else:
            Hash[x] = 1

    Hash = dict(
    sorted(Hash.items(), key=lambda item: item[1], reverse=True))
    for x in Hash.items():
        ret.append(x[0])
        if(len(ret) == k):
            break

    return ret

nums = [1,1,1,2,2,3]; k = 2
print(topKFrequent(nums,k))