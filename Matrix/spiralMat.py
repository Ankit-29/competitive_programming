# Spiral Matrix
'''
Given a 2D array, print it in spiral form.
e.g.
Input:
1    2   3   4
5    6   7   8
9   10  11  12
13  14  15  16
Output: 
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
'''
from typing import List


def spiralMat(mat: List[List[int]]) -> List[int]:
    row = len(mat)
    col = len(mat[0]) if mat[0] else 0
    spiral = list()
    for x in range(row//2+1):
        for y in range(x, col-x):
            spiral.append(mat[x][y])

        if(x!=(row//2)):
            for y in range(x+1, row-x):
                spiral.append(mat[y][col-x-1])

            for y in range(col-x-2, x-1, -1):
                spiral.append(mat[row-x-1][y])

            for y in range(row-x-2, x, -1):
                spiral.append(mat[y][x])

    return spiral


mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# mat = [
#     [1, 2, 3, 4, 5,  6],
#     [7, 8, 9, 10, 11, 12],
#     [13, 14, 15, 16,  17, 18],
# ]
print(spiralMat(mat))
