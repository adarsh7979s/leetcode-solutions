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

        current = head

        while prev is not None:
            if prev.val != current.val:
                return False

            else:
                prev = prev.next
                current = current.next
        return True

