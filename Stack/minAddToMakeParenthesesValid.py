'''
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) 
so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
Input: "())"
Output: 1

Input: "((("
Output: 3

Input: "()))(("
Output: 4

Input: "()"
Output: 0
'''
def minAddToMakeValid(S: str) -> int:
    stack = list()
    size = 0
    for x in S:
        if(x == "("):
            stack.append(x)
            size += 1
        else:
            if(size and stack[-1]=="("):
                stack.pop()
                size -= 1
            else:
                stack.append(x)
                size += 1   
    return size

S = "()))(("
print(minAddToMakeValid(S))