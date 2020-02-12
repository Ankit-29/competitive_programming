'''
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. 
t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
Input:
s = "abc", t = "ahbgdc"
Output:
True
'''

def isSubsequence(s: str, t: str) -> bool:
        i = j = 0
        if(len(s)==0):return True
        while(i!=len(s) and j<len(t)):
            if(s[i]==t[j]):
                i+=1
            
            j += 1
                
            if(i==len(s)):
                return True
        
        return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))
