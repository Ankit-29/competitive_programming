'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a 
letter in pattern and a non-empty word in str.
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
'''

def wordPattern(pattern: str,S:str) -> bool:
    d0 = {}; d1 = {}
    plist = list(pattern)
    slist = str.split(' ')
    if len(plist) != len(slist): return False 
    for ch, word in zip(plist, slist): 
        #print(ch, word)
        if ch not in d0:
            d0[ch] = word
        if word not in d1:
            d1[word] = ch
        if d0[ch] != word or d1[word] != ch:
            return False 
    return True 

pattern = "abba"
S = "dog cat cat dog"
print(wordPattern(pattern,S))