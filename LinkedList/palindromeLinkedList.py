'''
Given a singly linked list, determine if it is a palindrome.
Input: 1->2
Output: false
Input: 1->2->2->1
Output: true
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = list(); temp = head
        while(temp != None):
            stack.append(temp.val)
            temp = temp.next
        
        length = len(stack)//2
        lTemp = len(stack)
        temp = head
        
        while(temp != None):
            if(temp.val != stack.pop()):
                return False
            
            if(lTemp == length):
                return True
            
            temp = temp.next
            lTemp -= 1
        
        return True

# Driver Code
inputList  = ListNode(0)
curr = inputList
for x in [1,2,2,1]:
    newNode = ListNode(x)
    curr.next = newNode
    curr = curr.next

print(Solution().isPalindrome(inputList.next))