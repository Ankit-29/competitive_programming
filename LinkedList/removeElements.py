'''
Remove all elements from a linked list of integers that have value val.
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while(head !=None and head.val == val):
            head = head.next
            
        temp = head
        
        if(head == None):return head

        while(head.next != None):
            if(head.next.val == val):
                head.next = head.next.next  
            else:
                head = head.next
        
        return temp

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,2,6,3,4,5,6]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

val = 6
head = Solution().removeElements(inputList.next,val)
while(head != None):
    print(head.val,end=" ")
    head = head.next