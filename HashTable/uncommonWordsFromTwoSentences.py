'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''
from typing import List
def uncommonFromSentences(A: str, B: str) -> List[str]:
    Hash = dict()
    ret = list()
    for word in A.split():
        Hash[word] = Hash.get(word, 0) + 1
    for word in B.split():
        Hash[word] = Hash.get(word, 0) + 1
    
    for key in Hash.keys():
        if(Hash[key]==1):
            ret.append(key)
    
    return ret

A = "this apple is sweet"; B = "this apple is sour"
print(uncommonFromSentences(A,B))