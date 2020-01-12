# Valid Parentheses
# Time Complexity O(N)
# Function to check if parentheses are Valid or Balanced 
import re

def validParentheses(S):
    stack = list()
    auxDict = {')':'(', '}':'{',']':'['}
    for x in S:
        if(re.search(r"(\(|\{|\[)",x)):
            stack.append(x)
        elif(re.search(r"(\)|\}|\])",x)):
            if(not(len(stack))):return "Invalid"
            if(auxDict[x]==stack[-1]):
                stack.pop()
            else:
                stack.append(x)
    return "Invalid" if(len(stack)) else "Valid"

S = "[()]{}{[()()]()}" 
print(validParentheses(S))

