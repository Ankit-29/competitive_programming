'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum 
cost to reach the top of the floor, and you can either start from the step with index 0, 
or the step with index 1.
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
'''
from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    l = len(cost)
    for x in range(2,l):
        cost[x] += min(cost[x-1],cost[x-2])
    
    return min(cost[l-1],cost[l-2])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost))