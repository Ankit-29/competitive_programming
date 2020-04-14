'''
You have a list of words and a pattern, and you want to know which words in words matches the pattern.
A word matches the pattern if there exists a permutation of letters p so that after replacing every 
letter x in the pattern with p(x), we get the desired word.
(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another 
letter, and no two letters map to the same letter.)
Return a list of the words in words that match the given pattern. 
You may return the answer in any order.
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
'''
from typing import List
def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    ret = list()
    patHash = {}
    val = 1
    pat = ""
    for x in pattern:
        if(x not in patHash):
            patHash[x] = val
            val += 1
        pat += str(patHash[x])

    for word in words:
        wordHash = {}
        val = 1
        wordPat = ""
        for idx,letter in enumerate(word):
            if(letter not in wordHash):
                wordHash[letter] = val
                val += 1
            wordPat += str(wordHash[letter])
    
        if(wordPat==pat):ret.append(word)
                
    return ret

words = ["abc","deq","mee","aqq","dkd","ccc"]; pattern = "abb"
print(findAndReplacePattern(words,pattern))