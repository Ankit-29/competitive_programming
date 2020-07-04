'''
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''

from typing import List
def countCharacters(words: List[str], chars: str) -> int:
    Hash = makeHash(chars)
    ret = 0
    for word in words:
        wordHash = makeHash(word)
        isValid = True
        for key in wordHash.keys():
            if(key not in Hash):
                isValid = False
                break
            if(Hash[key]<wordHash[key]):
                isValid = False
                break
        if(isValid):
            ret += len(word)
    
    return ret
            


def makeHash(chars: str) -> dict:
    Hash = dict()
    for ch in chars:
        if(ch in Hash):
            Hash[ch] += 1
        else:
            Hash[ch] = 1
    
    return Hash

words = ["cat","bt","hat","tree"]; chars = "atach"
print(countCharacters(words,chars))