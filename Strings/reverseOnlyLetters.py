'''
Given a string S, return the "reversed" string where all characters that are not a
letter stay in the same place, and all letters reverse their positions.
Input: "ab-cd"
Output: "dc-ba"
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
'''

def reverseOnlyLetters(S: str) -> str:
        lst = list(S); l = 0; r = len(S)-1 
        while(l<r):
            while(not(lst[r].isalpha())):
                r -= 1
                if(r==l):
                    return "".join(lst)
            
            while(not(lst[l].isalpha())):
                l += 1
                if(r==l):
                    return "".join(lst)
            
            lst[r],lst[l] = lst[l],lst[r]
            
            r -= 1; l += 1
    
        return "".join(lst)

S = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(S))