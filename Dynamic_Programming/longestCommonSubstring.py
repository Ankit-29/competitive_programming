# Length of Longest Common Substring
'''
Given two strings find the length of the longest common substring.
'''
def longestCommonSubstringDp(str1: str, str2: str) -> int:
    row = len(str1)
    col = len(str2)
    dp = [[0]*(col+1) for x in range(row+1)]
    res = 0
    for x in range(1,row+1):
        for y in range(1,col+1):
            if(str1[x-1]==str2[y-1]):
                dp[x][y] = 1 + dp[x-1][y-1]
                res = max(res,dp[x][y])
            else:
                dp[x][y] = 0

    return res               

str1 = "abcdaf"
str2 = "zbcdf"
print(longestCommonSubstringDp(str1,str2))

