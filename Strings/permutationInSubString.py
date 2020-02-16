'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''

def permutationsInSubString(s1: str, s2: str) -> bool:
    Hash = [0]*26
    HashB = [0]*26
    l1 = len(s1)
    l2 = len(s2)
    for x in s1:
        Hash[ord(x)-ord('a')] += 1
    
    for x in range(l1):
        HashB[ord(s2[x])-ord('a')] += 1
            
    for x in range(l1,l2):
        for y in range(26):
            if(HashB[y]!=Hash[y]):
                break
            if(y==25):
                return True
        HashB[ord(s2[x-l1])-ord('a')] -= 1
        HashB[ord(s2[x])-ord('a')] += 1
    
    return False

s1 = "ab" 
s2 = "eidbaooo"
print(permutationsInSubString(s1,s2))