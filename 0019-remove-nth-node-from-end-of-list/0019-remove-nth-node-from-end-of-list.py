# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length = 0
        current = head
        while current != None:
            length +=1
            current = current.next
        k = length - n

        if k == 0:
            return head.next

            
        current = head
        for i in range(k-1):
           
            current = current.next
        current.next = current.next.next

        return head