# 90 Degree AntiClockWise Rotation (Inplace)
'''
Given a square matrix, Rotate its elements 90 Degree. 
e.g.
      Input          ||       Output  
1    2    3    4     ||  4    8    12   16 
5    6    7    8     ||  3    7    11   15 
9    10   11   12    ||  2    6    10   14
13   14   15   16    ||  1    5    9    13
'''

from typing import List

def rotate90Deg(mat: List[List[int]]) -> List[List[int]]:
    size = len(mat)
    for x in range(size-1,-1,-1):
        col = x
        row = size-x-1
        while(row<size and col>=0):
            mat[row][x],mat[size-x-1][col] = mat[size-x-1][col],mat[row][x]
            col -= 1
            row += 1

    return mat

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotatedMat = rotate90Deg(mat)
for row in rotatedMat:
    print(row)