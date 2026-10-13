# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        dummy = ListNode(0)
        current = dummy

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        current = slow
        prev = None

        while current is not None:
            nextnode = current.next
            current.next = prev
            prev = current 
            current = nextnode

        curr1 = prev
        curr2 = head
        while curr1 is not None:
            if curr1.val != curr2.val:
                return False

            else:
                curr1 = curr1.next
                curr2 = curr2.next

        return True




