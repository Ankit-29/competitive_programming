# Length Longest Common Subsequences
'''
    Given two sequences, find the length of longest subsequence present in 
    both of them.A subsequence is a sequence that appears in the same 
    relative order, but not necessarily contiguous. e.g. “abc”, “abg”, 
    “bdf”, ”acefg”, .. etc are subsequences of “abcdefg”.
'''

def longestCommonSubsequenceDp(str1: str, str2: str) -> int:
    row = len(str1)
    col = len(str2)
    dp = [[0]*(col+1) for x in range(row+1)]
    for x in range(1,row+1):
        for y in range(1,col+1):
            if(str1[x-1]==str2[y-1]):
                dp[x][y] = 1 + dp[x-1][y-1]
            else:
                dp[x][y] = max(dp[x-1][y],dp[x][y-1])

    return dp[row][col]                    

str1 = "abcdaf"
str2 = "acbcf"
print(longestCommonSubsequenceDp(str1,str2))

