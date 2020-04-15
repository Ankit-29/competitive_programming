'''
A string S of lowercase letters is given. We want to partition this string into as many parts as 
possible so that each letter appears in at most one part, and return a list of integers representing 
the size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts
'''
from typing import List
def partitionLabels(S: str) -> List[int]:
    lastIdxHash = dict()
    ret = list()
    lastIdx = 0; lenCovered = 0
        
    for idx,val in enumerate(S):
        lastIdxHash[val] = idx
    
    
    for idx,val in enumerate(S):
        lastIdx = max(lastIdx,lastIdxHash[val])
        if(lastIdx==idx):
            ret.append(lastIdx - lenCovered + 1)
            lenCovered = idx + 1
    
    return ret

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))