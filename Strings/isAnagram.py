'''
Given two strings s and t , write a function to determine if t is an anagram of s.
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
'''


def isAnagram(s: str, t: str) -> bool:
    Hash = [0]*26
    for x in s:
        Hash[ord(x)-ord('a')] +=1
        
    for x in t:
        Hash[ord(x)-ord('a')] -=1
    
    valSum = 0
    for x in range(26):
        valSum += abs(Hash[x]) 
    
    
    return True if valSum==0 else False

s = "anagram"; t = "nagaram"
print(isAnagram(s,t))