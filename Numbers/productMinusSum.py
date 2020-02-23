'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
'''


def subtractProductAndSum(n: int) -> int:
        pro = 1; add = 0 
        while(n):
            rem = n % 10
            pro *= rem
            add += rem
            n //=10
        
        return pro-add

n = 234
print(subtractProductAndSum(n))