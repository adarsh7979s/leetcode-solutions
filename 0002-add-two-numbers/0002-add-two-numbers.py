class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # curr1 = l1
        # curr2 = l2

        # arr1 = []
        # arr2 = []

        # while curr1 is not None:
        #     arr1.append(curr1.val)
        #     curr1 = curr1.next

        # while curr2 is not None:
        #     arr2.append(curr2.val)
        #     curr2 = curr2.next

        # d1 = int("".join(map(str, arr1[::-1])))
        # d2 = int("".join(map(str, arr2[::-1])))

        # total = d1 + d2

        # revsum = str(total)[::-1]

        # dummy = ListNode(0)
        # current = dummy

        # for digit in revsum:
        #     current.next = ListNode(int(digit))
        #     current = current.next

        # return dummy.next


        dummy = ListNode(0)
        current = dummy
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 is not None or curr2 is not None:
            val1= curr1.val if curr1 is not None else 0
            val2 = curr2.val if curr2 is not None else 0

            

            total = val1 + val2 + carry 

            digit = total % 10
            carry = total // 10

            current.next = ListNode(digit)
            current = current.next

            if curr1 is not None:
                curr1 = curr1.next

            if curr2 is not None:
                curr2 = curr2.next

        if carry != 0:
            current.next = ListNode(carry)

        return dummy.next

