'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''
from typing import List

def letterCasePermutation(S: str) -> List[str]:
        return list(backTrack(list(S),0,len(S),list()))

def backTrack(S, left, right, ret)-> List[str]:
    if(left == right):
        ret.append("".join(S[::]))
    else:
        if(S[left].isnumeric()):
            backTrack(S, left+1, right, ret)
        else:
            S[left] = S[left].upper()
            backTrack(S, left+1, right, ret)
            
            S[left] = S[left].lower()
            backTrack(S, left+1, right, ret)

    return ret

S = "a1b2"
print(letterCasePermutation(S))