'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
'''

def hasAlternatingBits(n: int) -> bool:
    lastBit = n & 1
    while(n):
        n //= 2
        currBit = n & 1
        if(not(lastBit ^ currBit)):
            return False
        
        lastBit = (n & 1)
    
    return True

n = 5
print(hasAlternatingBits(n))