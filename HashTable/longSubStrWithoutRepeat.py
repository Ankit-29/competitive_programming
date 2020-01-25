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
        left = 0 # Left most index of current substring
        Hash = dict()
        for x in range(len(s)):
            # Check if character already present 
            if(s[x] in Hash):
                # Change Left index
                left = max(Hash[s[x]]+1,left) 
            
            # Update Hash
            Hash[s[x]] = x
            
            # Calculate longest length
            longest = max(longest,x - left + 1) 
            
        return longest

s = "tmmzuxt"
print(lengthOfLongestSubstring(s))

