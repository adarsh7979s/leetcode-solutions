# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        current = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        total = 0
        while curr1 is not None or curr2 is not None:
            if curr1 is not None:
                val1 = curr1.val
                curr1 = curr1.next
            else:
                val1 = 0
            if curr2 is not None:
                val2 = curr2.val
                curr2 = curr2.next

            else:
                val2 = 0

            total = val1 + val2 +carry

            digit = total % 10
            carry = total//10

        
            current.next = ListNode(digit)
            current = current.next

        if carry != 0:
            current.next = ListNode(carry)
        
        return dummy.next


            