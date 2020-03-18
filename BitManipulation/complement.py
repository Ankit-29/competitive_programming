'''
Given a positive integer, output its complement number. The complement strategy 
is to flip the bits of its binary representation.
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),and its complement is 010 (2).
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0 (0). 
'''

def findComplement(num: int) -> int:
    placeVal = 1
    complement = 0
    while(num):
        complement += 0 if(num & 1) else (1*placeVal)
        placeVal <<=1
        num >>=1
    
    return complement

num = 5
print(findComplement(num))