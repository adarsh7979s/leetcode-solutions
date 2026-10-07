# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        length = 0
        current = head 

        while current is not None:
            current = current.next
            length +=1

        index = length - k

        first = head
        for i in range(k-1):
            first = first.next

        second = head
        for i in range(index):
            second = second.next
        
        temp = first.val       
        first.val = second.val
        second.val = temp
                        # OR
        # Pyhton lets you swap directly (Tuple Unpacking)
        # first.val, second.val = second.val, first.val
        
        return head
            