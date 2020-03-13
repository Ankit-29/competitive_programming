'''
Reverse a singly linked list.
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None; nextNode = None; curr = head
        while(curr != None):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        head = prev        
        return head

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,2,3,4,5]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

reversedList = Solution().reverseList(inputList.next)
while(reversedList != None):
    print(reversedList.val,end=" ")
    reversedList = reversedList.next