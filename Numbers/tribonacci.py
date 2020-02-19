'''
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
Input: n = 4
Output: 4
Input: n = 25
Output: 1389537
'''

def tribonacci(n: int) -> int:
    if(n==0):return 0
    if(n<3):return 1
    
    dp = [0]*(n+1)
    
    dp[1] = dp[2] = 1

    for x in range(3,n+1):
        dp[x] = dp[x-1]+dp[x-2]+dp[x-3]
    
    return dp[n]

n = 25
print(tribonacci(n))
