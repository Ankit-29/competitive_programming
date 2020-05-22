'''
Given a string s. You should re-order the string using the following algorithm:
- Pick the smallest character from s and append it to the result.
- Pick the smallest character from s which is greater than the last appended character to the result and append it.
- Repeat step 2 until you cannot pick more characters.
- Pick the largest character from s and append it to the result.
- Pick the largest character from s which is smaller than the last appended character to the result and append it.
- Repeat step 5 until you cannot pick more characters.
- Repeat the steps from 1 to 6 until you pick all characters from s.
- In each step, If the smallest or the largest character appears more than once you can choose any occurrence and 
  append it to the result.

Return the result string after sorting s with this algorithm.

Constraints:
- 1 <= s.length <= 500
- s contains only lower-case English letters.

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Input: s = "rat"
Output: "art"
'''

def sortString(s: str) -> str:
    frequency = [0]*26
    ans = ""; lengthAns = 0; lengthS = len(s)
    
    for char in s: 
        frequency[ord(char)-ord('a')] += 1

    while(lengthAns != lengthS):
        for idx in range(0,26):
            if(frequency[idx]!=0):
                ans += chr(idx+ord('a'))
                lengthAns += 1
                frequency[idx] -= 1

        for idx in range(26-1,-1,-1):
            if(frequency[idx]!=0):
                ans += chr(idx+ord('a'))
                lengthAns += 1
                frequency[idx] -= 1
    
    return ans


s = "aaaabbbbcccc"
print(sortString(s))
