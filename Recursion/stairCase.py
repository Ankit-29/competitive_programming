# Total ways to reach the n’th stair
'''
There are n stairs, a person standing at the bottom wants to reach the top. 
The person can climb either 1 stair or 2 stairs at a time. Count the number 
of ways, the person can reach the top.
Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
'''
def noOfWays(n:int)->int:
    if(n<=1):
        return 1
    
    return noOfWays(n-1)+noOfWays(n-2)

n = 4
print(noOfWays(4))
