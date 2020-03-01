'''
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array 
in-place with O(1) extra memory.
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

from typing import List

def reverseString(s: List[str]) -> List[str]:
    l = len(s)
    mid = (l//2)+1 if l%2!=0 else l//2
    for x in range(0,mid):
        s[x],s[l-x-1] = s[l-x-1],s[x]

    return s

s = ["h","e","l","l","o"]
print(reverseString(s))