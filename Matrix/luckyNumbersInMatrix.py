'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
'''

from typing import List

def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    Hash = {
        'row': [],
        'col': []
    }

    ret = []
    for x in range(0, len(matrix)):
        Hash['row'].append(min(matrix[x]))

    for x in range(0, len(matrix[0])):
        m = 0
        for y in range(0, len(matrix)):
            m = max(m, matrix[y][x])
        Hash['col'].append(m)

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if(matrix[x][y] == Hash['row'][x] and matrix[x][y] == Hash['col'][y]):
                ret.append(matrix[x][y])

    return ret


matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(luckyNumbers(matrix))