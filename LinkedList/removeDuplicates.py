'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2
Output: 1->2
Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head == None):
            return head       
        firstNode = head
        while(head.next != None):
            if(head.next.val == head.val):
                head.next = head.next.next
            else:
                head = head.next
                
        return firstNode

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,1,2,3,3]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

head = Solution().deleteDuplicates(inputList.next)
while(head != None):
    print(head.val,end=" ")
    head = head.next