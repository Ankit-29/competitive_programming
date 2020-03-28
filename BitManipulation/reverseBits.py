'''
Reverse bits of a given 32 bits unsigned integer.
Input: 43261596
Output: 964176192
Explanation: The input binary string 00000010100101000001111010011100 
             represents the unsigned integer 43261596 so return 964176192 
             which its binary representation is 00111001011110000010100101000000.

Input: 4294967293
Output: 3221225471
'''

def reverseBits(n: int) -> int:
    val = 0
    powTwo = 2**31
    while(n):     
        if(n & 1):
            val += powTwo
    
        powTwo //=2
        n //=2
        
    return val

n =  43261596
print(reverseBits(n))