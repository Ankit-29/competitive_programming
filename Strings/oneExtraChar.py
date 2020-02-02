# One Missing Character
'''
Given two strings which are of lengths n and n+1. The second string contains
all the character of the first string, but there is one extra character. 
Your task to find the extra character in the second string.
Input : string strA = "abcd";
        string strB = "cbdae";
Output : e
'''
def oneExtraChar(strA: str, strB: str) -> str:
    freq = [0]*26
    for x in strA:
        freq[ord(x)-ord('a')] += 1

    for x in strB:
        freq[ord(x)-ord('a')] -= 1

    for x in range(len(freq)):
        if(abs(freq[x])):
            return chr(97+x)

strA = "abcd"
strB = "cbdae"
print(oneExtraChar(strA,strB))


