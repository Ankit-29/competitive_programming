# Minimum operation to make all elements equal in array
'''
Given an array with n positive integers.We need to find the minimum 
number of operation to make all elements equal.We can perform 
addition, multiplication, subtraction or division with any element 
on an array element.
'''
def minOperations(arr: list) -> int:
    Hash = dict()
    N = len(arr)
    maxFreq = 0              # Maximum Frequency 
    for x in range(N):
        Hash[arr[x]] = Hash[arr[x]] + 1 if arr[x] in Hash else 1
        maxFreq = max(Hash[arr[x]],maxFreq)
    
    return N - maxFreq

arr = [1, 5, 2, 1, 3, 2, 1]
print(minOperations(arr))
