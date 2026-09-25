# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         """
#         :type head: Optional[ListNode]
#         :type n: int
#         :rtype: Optional[ListNode]
#         """
#         length = 0
#         current = head
#         while current != None:
#             length +=1
#             current = current.next
#         k = length - n

#         if k == 0:
#             return head.next


#         current = head
#         for i in range(k-1):
           
#             current = current.next
#         current.next = current.next.next

#         return head

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Move both until fast reaches the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next