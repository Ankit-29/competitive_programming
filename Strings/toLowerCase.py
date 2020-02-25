'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Input: "Hello"
Output: "hello"
'''

def toLowerCase(s: str) -> str:
    s = list(s)
    for x in range(len(s)):
        cAscii = ord(s[x])
        if(cAscii>=65 and cAscii<=90):
            s[x] = chr(cAscii+32)
    
    return "".join(s)


s = "Hello"
print(toLowerCase(s))

