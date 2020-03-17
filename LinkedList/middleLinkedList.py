'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Note:
The number of nodes in the given list will be between 1 and 100.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if(head.next==None):return head
        fastPtr = head
        slowPtr = head
        while(fastPtr != None and fastPtr.next != None):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
                
        return slowPtr

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,2,3,4,5,6]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

middleNode = Solution().middleNode(inputList.next)
while(middleNode != None):
    print(middleNode.val,end=" ")
    middleNode = middleNode.next