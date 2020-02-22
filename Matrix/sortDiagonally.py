'''
Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to 
the bottom-right then return the sorted array.
Input: mat = 
   [[3,3,1,1],
    [2,2,1,2],
    [1,1,1,2]]
Output: 
   [[1,1,1,1],
    [1,2,2,2],
    [1,2,3,3]]
'''
from typing import List
def diagonalSort(mat: List[List[int]]) -> List[List[int]]:
    m = len(mat) 
    n = len(mat[0])
    for x in range(0,n):           
        tempRow = 0; tempCol = x
        tempList = list()
        while(tempCol<n and tempRow<m):
            tempList.append(mat[tempRow][tempCol])
            tempCol +=1
            tempRow +=1
        tempList.sort()
        
        tempRow = 0; tempCol = x; i = 0
        while(tempCol<n and tempRow<m):
            mat[tempRow][tempCol] = tempList[i] 
            tempCol +=1
            tempRow +=1
            i += 1

    for x in range(1,m):
        tempCol = 0; tempRow = x
        tempList = list()
        while(tempCol<n and tempRow<m):
            tempList.append(mat[tempRow][tempCol])
            tempCol +=1
            tempRow +=1
        tempList.sort()
        
        tempCol = 0; tempRow = x; i = 0
        while(tempCol<n and tempRow<m):
            mat[tempRow][tempCol] = tempList[i]
            tempCol +=1
            tempRow +=1
            i+=1

    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(diagonalSort(mat))