# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        carry = 0
        head = ListNode(0)
        current = head
        while(l1 or l2):
            val = carry
            
            # Find a sum of two value
            if l1 and l2:
                val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val += l1.val
                l1 = l1.next
            elif l2:
                val += l2.val
                l2 = l2.next
            
            current.next = ListNode(val % 10)
            
            if val >= 10:
                carry = 1
            else:
                carry = 0
                
            current = current.next
        
        if (carry == 1):
            current.next = ListNode(1)
            
        return head.next
