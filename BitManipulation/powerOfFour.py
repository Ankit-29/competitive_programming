'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
Input: 16
Output: True
Input: 5
Output: False
'''
def isPowerOfFour(num: int) -> bool:
    totalOne = 0
    bitPos  = 1
    lastX = 0
    for x in range(0,32):
        if(num & bitPos):
            totalOne += 1
            lastX = x
            
        bitPos <<= 1
    
    return True if totalOne==1 and lastX%2==0 else False

num = 256
print(isPowerOfFour(num))
