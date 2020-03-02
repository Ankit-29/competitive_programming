'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation: In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
'''

from typing import List
def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    for x in range(1,len(matrix)):
        for y in range(1,len(matrix[0])):
            if(matrix[x-1][y-1]!=matrix[x][y]):
                return False
    
    return True

matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(isToeplitzMatrix(matrix))

