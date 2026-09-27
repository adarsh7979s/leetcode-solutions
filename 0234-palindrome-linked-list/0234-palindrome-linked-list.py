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
        # current = head
        # arr = []
        # while current is not None:
        #     arr.append(current.val)
        #     current = current.next
           
        # if arr == arr[::-1]:
        #     return True

        # else:
        #     return False

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

        current1 = head
        while prev is not None:
            if current1.val == prev.val:
                current1 = current1.next
                prev = prev.next
            else:
                return False
        return True


        
                
           
            



            
