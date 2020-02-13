'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Inputs:          |   Outputs 
[1,2,3]          |   [1,2,4]   
[4,3,2,1]        |   [4,3,2,2]
[9]              |   [1,0]
[8,9,9,9]        |   [9,0,0,0]
'''
from typing import List
def plusOne(digits: List[int]) -> List[int]:
    l = len(digits)
    if(digits[l-1]<9):
        digits[l-1] +=1
        return digits
    digits[l-1] = 0
    carry = 1
    for x in range(l-2,-1,-1):
        if(digits[x]==9):
            digits[x] = 0
            carry = 1
        else:
            digits[x] += carry
            carry = 0
            break
    if(carry):
        digits = [1] + digits
    return digits

print(plusOne([8,9,9,9]))