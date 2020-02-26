'''
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.
Input: "A man, a plan, a canal: Panama"
Output: true
Input: "race a car"
Output: false
'''
import re

def isPalindromeRegex(s: str) -> bool:
        s=s.lower()
        temp = ""
        regex = r"(\w|\d)"
        for x in s:
            if(re.search(regex,x)):
                temp += x
                
        return True if temp==temp[::-1] else False

def isPalindrome(s: str) -> bool:
    s=s.lower()
    temp = ""
    for x in s:
        if(ord(x)>=97 and ord(x)<=122 or ord(x)>=48 and ord(x)<=57):
            temp += x
    return True if temp==temp[::-1] else False

s = "A man, a plan, a canal: Panama"
print(isPalindromeRegex(s))
print(isPalindrome(s))