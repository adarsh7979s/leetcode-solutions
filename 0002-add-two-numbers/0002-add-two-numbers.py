class Solution(object):
    def addTwoNumbers(self, l1, l2):

        curr1 = l1
        curr2 = l2

        arr1 = []
        arr2 = []

        while curr1 is not None:
            arr1.append(curr1.val)
            curr1 = curr1.next

        while curr2 is not None:
            arr2.append(curr2.val)
            curr2 = curr2.next

        d1 = int("".join(map(str, arr1[::-1])))
        d2 = int("".join(map(str, arr2[::-1])))

        total = d1 + d2

        revsum = str(total)[::-1]

        dummy = ListNode(0)
        current = dummy

        for digit in revsum:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next