'''
Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
'''

from typing import List
def findWords(words: List[str]) -> List[str]:
    Hash = {
        1: {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1},
        2: {'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2},
        3: {'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
    }

    ret = list()
    for word in words:
        temp = word.lower()
        lastLine = 0
        flag = True

        if(temp[0] in Hash[1]):
            lastLine = 1
        elif(temp[0] in Hash[2]):
            lastLine = 2
        else:
            lastLine = 3

        for x in temp:
            if(x in Hash[1]):
                curLine = 1
            elif(x in Hash[2]):
                curLine = 2
            else:
                curLine = 3

            if(curLine != lastLine):
                flag = False
                break

        if(flag):
            ret.append(word)

    return ret

words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))