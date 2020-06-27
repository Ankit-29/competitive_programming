'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

from typing import List
def sortArrayByParityII(A: List[int]) -> List[int]:
	ret = A[::]
	e = 0; o = 1
	for x in A:
		if(x%2==0):
			ret[e] = x
			e += 2
		else:
			ret[o] = x
			o += 2

	return ret

A = [4,2,5,7]
print(sortArrayByParityII(A))
