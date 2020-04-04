'''
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.
The trace of a square matrix is the sum of the values on the main diagonal 
(which runs from the upper left to the lower right). An N-by-N square matrix is a Latin square 
if each cell contains one of N different values, and no value is repeated within a row or a column. 
In this problem, we will deal only with "natural Latin squares" in which the N values are the integers 
between 1 and N.
Given a matrix that contains only integers between 1 and N, we want to compute its
trace and check whether it is a natural Latin square. To give some additional
information, instead of simply telling us whether the matrix is a natural Latin square
or not, please compute the number of rows and the number of columns that contain
repeated values.
Input: N = 4; mat = [[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]]
Output: 9 4 4
Explanation: Order of output- Sum of diagonal, Repeated rows, Repeated columns 
Input: N = 3; mat = [[2,1,3],[1,3,2],[1,2,3]]
Output: 8 0 2
'''
from typing import List
def vestigium(mat: List[int],n: int)->List[int]:
    HashRow = {}; HashCol = {}; repeatRow = 0; repeatCol=0; trace = 0
    for x in range(n):
        HashRow[x] = {}
        for y in range(n):
            if(y not in HashCol):
                HashCol[y] = {}
            trace += mat[x][y] if x==y else 0

            if('-1' not in HashRow[x] and mat[x][y] in HashRow[x]):
                repeatRow += 1
                HashRow[x]['-1'] = 1
            else:
                HashRow[x][mat[x][y]] = 1
            
            if('-1' not in HashCol[y] and mat[x][y] in HashCol[y]):
                repeatCol += 1
                HashCol[y]['-1'] = 1
            else:
                HashCol[y][mat[x][y]] = 1

    return [trace,repeatRow,repeatCol]

n = 4; mat = [[2,2,2,2],[2,3,2,3],[2,2,2,3],[2,2,2,2]]
print(vestigium(mat,n))