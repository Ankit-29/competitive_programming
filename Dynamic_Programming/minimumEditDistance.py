# Minimum Edit Distance
'''
Given two strings str1 and str2 and below operations that can performed on str1. 
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
- Insert
- Remove
- Replace
'''

def minEditDistance(str1: str, str2: str) -> int:
    col = len(str1)
    row = len(str2)
    dp = [[0]*(col+1) for x in range(row+1)]
    # Initializing row[0] and col[0]
    for x in range(row+1):
        dp[x][0] = x
    for y in range(col+1):
        dp[0][y] = y

    # Fill Dp Matrix
    for x in range(1,row+1):
        for y in range(1,col+1):
            if(str2[x-1]==str1[y-1]):
                dp[x][y] = dp[x-1][y-1]  
            else:
                dp[x][y] = 1 + min(dp[x-1][y-1],dp[x-1][y],dp[x][y-1])

    return dp[row][col]

str1 = "abcdef"
str2 = "azced"
print(minEditDistance(str1,str2))

