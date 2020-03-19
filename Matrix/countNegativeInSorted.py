'''
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
Return the number of negative numbers in grid.
Input: grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]
Output: 8
'''

from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    sizeRow = len(grid)
    sizeCol = len(grid[0]) if(sizeRow>0) else 0
    r = 0; count = 0 
    while(r<sizeRow):
        c = sizeCol-1
        if(grid[r][0]<0):
            count += sizeCol
        elif(grid[r][c]>=0):
            count += 0
        else:
            while(c>=0):
                if(grid[r][c]>=0):
                    count += sizeCol - c - 1
                    break
                c -= 1
        r += 1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))