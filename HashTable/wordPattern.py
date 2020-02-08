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
    Hash = dict()
    HashTwo = dict()        
    words = S.split()
    if(len(words)!=len(pattern)):
        return False

    for x in range(len(pattern)):
        ch = pattern[x]
        word = words[x]
        if(ch not in Hash):
            Hash[ch] = word
        if(word not in HashTwo):
            HashTwo[word] = ch

        if(Hash[ch] != word or HashTwo[word] != ch):
            return False
        
    return True

pattern = "abba"
S = "dog cat cat dog"
print(wordPattern(pattern,S))