'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: 6 - 1 = 5

Input: [7,6,4,3,1]
Output: 0
'''
from typing import List

def maxProfit(prices: List[int]) -> int:
    minIdx = 0 
    best = 0
    for x in range(0,len(prices)):
        if(prices[minIdx]>prices[x]):
            minIdx = x 
        best = max(best,prices[x]-prices[minIdx])
    return best

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

