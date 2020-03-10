'''
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. 
(Trailing spaces are not allowed).Each word would be put on only one column and that in one 
column there will be only one word.
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
'''
from typing import List
def printVertically(self, s: str) -> List[str]:
    wordList = s.split()
    l = 0
    for x in wordList:
        l = max(len(x),l)   
    ret = list() 
    for x in range(l):
        temp = ""
        for y in range(len(wordList)):                
            temp += wordList[y][x] if(len(wordList[y])>x) else " "
            
        ret.append(temp.rstrip())
    
    return ret