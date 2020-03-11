'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list 
is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
'''

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nodeVal = list()
        l = 0
        while(head!=None):
            nodeVal.append(head.val)
            l +=1
            head = head.next
        
        
        power = 2**(l-1)
        dec = 0
        for x in nodeVal:
            dec += x*power
            power //=2

        return dec

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,0,1]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

print(Solution().getDecimalValue(inputList.next))