'''
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, 
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. 
For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.
Return the number of different transformations among all words we have.
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
'''
from typing import List
def uniqueMorseRepresentations(words: List[str]) -> int:
    morseCodeList = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
        "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]
    Hash = dict()
    count = 0
    for word in words:
        morseCode = ""
        for letter in word:
            morseCode += morseCodeList[ord(letter)-ord('a')]

        if(morseCode not in Hash):
            Hash[morseCode] = morseCode
            count += 1

    return count


words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
