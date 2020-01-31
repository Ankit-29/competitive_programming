# Missing characters to make a string Panagram
'''
Given a string, find all characters that are missing from the string, i.e., 
the characters that can make string a Pangram. We need to print output in 
alphabetic order.
Input: "The quick brown fox jumps"
Output: "adglvyz"
'''
from typing import List
def missingCharactersInPanagram(S: str) -> List[str]:
    Hash = [0]*26
    for x in S.lower():
        if(x!=' '):
            Hash[ord(x)-ord('a')] += 1
    missingChars = [chr(97+x) for x in range(0,26) if Hash[x]==0]
    return missingChars

S = "The quick brown fox jumps"
print("".join(missingCharactersInPanagram(S)))
