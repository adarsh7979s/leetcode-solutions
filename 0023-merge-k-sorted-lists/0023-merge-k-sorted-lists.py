# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        values = []

        for node in lists:
            while node is not None:
                values.append(node.val)
                node = node.next

        sort = sorted(values)

        dummy = ListNode(0)
        current = dummy

        for i in sort:
            current.next = ListNode(i)
            current = current.next

        return dummy.next
