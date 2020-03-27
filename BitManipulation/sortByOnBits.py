'''
Given an integer array arr. You have to sort the integers in the array in ascending order by 
the number of 1's in their binary representation and in case of two or more integers have the 
same number of 1's you have to sort them in ascending order.
Return the sorted array.
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
'''
from typing import List
def sortByBits(arr: List[int]) -> List[int]:
    store = list()
    for x in arr:
        temp = x
        bitCount = 0 
        while(temp):
            bitCount += 1 if(temp & 1) else 0
            temp //= 2
        
        store.append([bitCount,x])
    
    store.sort(key=lambda x:(x[0],x[1]))
    
    return [x[1] for x in store]

arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))