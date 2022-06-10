"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        firstNode = ListNode()
        previousNode = firstNode
        whole = 0
        
        while l1 or l2 or whole > 0:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()
                
        
            remainder = (l1.val + l2.val + whole) % 10
            whole = (l1.val + l2.val + whole) // 10

            l1 = l1.next
            l2 = l2.next
            
            newNode = ListNode()
            newNode.val = remainder
            previousNode.next = newNode
            previousNode = newNode

        return firstNode.next
        
