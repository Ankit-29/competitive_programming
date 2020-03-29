'''
Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], 
for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] 
xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
'''
from typing import List
def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
        ret = list(); preXor = list()
        preXor.append(arr[0])
        for x in range(1,len(arr)):
            preXor.append(preXor[x-1] ^ arr[x])
            
        for query in queries:
            if(query[0]==0):
                ret.append(preXor[query[1]])
            else:
                ret.append(preXor[query[0]-1]^preXor[query[1]])
        
        return ret

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr,queries))