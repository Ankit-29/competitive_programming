# 0/1 Knapsack Problem (Dynamic Programming)
'''
Given weights and values of n items, we need to put these items in a knapsack 
of capacity W to get the maximum total value in the knapsack. we cannot 
break items.
'''

def knapSackDP(bagSize: int, items:list) -> int:
    dp = [[0]*(bagSize+1) for x in range(len(items)+1)]
    for x in range(1,len(items)+1):
        for y in range(1,bagSize+1):
            if(y<items[x-1][1]):
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = max(dp[x-1][y],items[x-1][0]+dp[x-1][y-items[x-1][1]])

    return dp[len(items)][bagSize]

# Structure of List: [(V1,W1),(V2,W2),...(Vn,Wn)]
items = [(10, 2), (5, 3), (15, 5), (7, 7), (6, 1), (18, 4), (3, 1)]
bagSize = 15
print(knapSackDP(bagSize, items))