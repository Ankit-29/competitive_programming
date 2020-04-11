'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English 
lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
'''
def mappingAlphabets(s: str) -> str:
    stack = list()
    x =len(s)-1
    while(x>=0):
        if(s[x]=='#'):
            intMap = (int(s[x-2])*10)+int(s[x-1])
            x -= 3
        else:
            intMap = int(s[x])
            x-=1
            
        stack.append(chr(ord('a')+intMap-1))            
    
    ret = ""
    while(stack):
        ret += stack.pop()
    
    return ret

s = "10#11#12"
print(mappingAlphabets(s))