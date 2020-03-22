'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
Note:
0 <= x, y < 2^31.
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
'''

def hammingDistance(x: int, y: int) -> int:
    count = 0
    while(x or y):
        count += 1 if (x & 1)!=(y & 1) else 0
        x //= 2
        y //= 2
    
    return count

x = 1; y = 4
print(hammingDistance(x,y))
        