'''
A self-dividing number is a number that is divisible by every digit it contains.
e.g. 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, 
including the bounds if possible.
Input: left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
'''
from typing import List
def selfDividingNumbers(left: int, right: int) -> List[int]:
    result = list()
    for x in range(left,right+1):
        flag = True
        temp = x
        while(temp):
            rem = temp%10
            if(rem==0 or x%rem!=0):
                flag = False
                break
        
            temp = temp//10
            
        if(flag):
            result.append(x)
            
    return result

left = 1
right = 22
print(selfDividingNumbers(left,right))