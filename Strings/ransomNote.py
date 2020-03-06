'''
Given an arbitrary ransom note string and another string containing letters from 
all the magazines, write a function that will return true if the ransom note can
be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

def canConstruct(ransomNote: str, magazine: str) -> bool:
    Hash = [0]*26
    for x in magazine:
        Hash[ord(x)-ord('a')] += 1
    
    for x in ransomNote:
        key = ord(x)-ord('a')
        if(Hash[key]>0):
            Hash[key] -= 1
        else:
            return False
    
    return True

print(canConstruct("aa", "aab"))
