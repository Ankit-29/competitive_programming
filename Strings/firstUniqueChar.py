'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.
s = "firstunique"
return 0.
s = "codecoder",
return 8.
'''

def firstUniqChar(s: str) -> int:
    Hash = dict()
    for x in range(len(s)):
        if(s[x] in Hash):
            Hash[s[x]] = -1
        else:
            Hash[s[x]] = x        
    
    for x in Hash.keys():
        if(Hash[x]!=-1):
            return Hash[x]
        
    return -1

s = "firstunique"
print(firstUniqChar(s))
