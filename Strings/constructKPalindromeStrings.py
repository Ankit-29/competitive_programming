'''
Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.
Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
'''

def canConstruct(s: str, k: int) -> bool:
    lenS = len(s)
    if(k>lenS):return False
    if(k==lenS):return True    
    frequency = [0]*26; odd = 0
    for char in s:
        frequency[ord(char)-ord('a')] += 1
        
    for val in frequency:
        if(val%2!=0):
            odd += 1
            if(odd>k):
                return False
    return True

s = "annabelle"; k = 2
print(canConstruct(s,k))