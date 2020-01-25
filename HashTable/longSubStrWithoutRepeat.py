# Longest Substing without Repeating Characters
'''
Given a string, find the length of the longest substring without 
repeating characters. e.g.
"pwwkew" -> 3
"dvdf" -> 3
"abcabcbb" -> 3
"bbbbb" -> 1
"abba" -> 2
"tmmzuxt" -> 5
'''
def lengthOfLongestSubstring(s: str) -> int:
        longest = 0
        left = 0
        Hash = dict()
        for x in range(len(s)):
            if(s[x] in Hash):
                left = max(Hash[s[x]]+1,left)
            Hash[s[x]] = x
            longest = max(longest,x - left + 1) 
            
        return longest

s = "tmmzuxt"
print(lengthOfLongestSubstring(s))

