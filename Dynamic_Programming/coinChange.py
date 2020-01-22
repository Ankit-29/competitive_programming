# Coin Change Problem (No of ways to make change)
'''
Given a value N, if we want to make change for amount N, and we 
have infinite supply of {c1,c2,c3} coins, In how many ways we 
can make the change? The order of coins doesn’t matter.
'''
def coinChange(coins: list, amount: int) -> int:
    row = len(coins)+1
    dp = [[0]*(amount+1) for x in range(row)]
    dp[0][0] = 1
    for x in range(1,row):
        dp[x][0] = 1
        for y in range(1,amount+1):
            if(coins[x-1]>y):
                dp[x][y] = dp[x-1][y]
            else:
                dp[x][y] = dp[x-1][y]+dp[x][y-coins[x-1]]

    return dp[row-1][amount]

coins = [1,5,6,8]
amount = 11
print(coinChange(coins,amount))
