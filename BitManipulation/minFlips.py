'''
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits 
of a and b to make ( a OR b == c ).Flip operation consists of change any single bit 
1 to 0 or change the bit 0 to 1 in their binary representation.
Input: a = 2, b = 6, c = 5  Output: 3
Explanation:0010 | 0110 = 0110 i.e 3 
            After Changes in a and b 
            0001 | 0100 = 0101 i.e 5
            So total Flips/Changes = 3 
'''
def minFlips(a: int, b: int, c: int) -> int:
    count = 0
    Hash = {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (0, 1, 0): 1,
        (0, 1, 1): 0,
        (1, 0, 0): 1,
        (1, 0, 1): 0,
        (1, 1, 0): 2,
        (1, 1, 1): 0
    }
    while(a or b or c):
        key = (a & 1, b & 1, c & 1)
        count += Hash[key]
        a >>= 1; b >>= 1; c >>= 1
    return count

a = 2; b = 6; c =5
print(minFlips(a,b,c))
