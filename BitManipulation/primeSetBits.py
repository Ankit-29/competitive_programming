'''
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having a 
prime number of set bits in their binary representation.
Input: L = 6, R = 10
Output: 4
Explanation:
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
'''


def countPrimeSetBits(L: int, R: int) -> int:
    primes = [0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0]
    count = 0
    for x in range(L,R+1):
        setBits = 0
        while(x):
            setBits += x & 1
            x >>=1
            
        if(primes[setBits]):
            count += 1
    
    return count

L = 6; R = 10
print(countPrimeSetBits(L,R))