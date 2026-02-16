class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        // Step 1: Create dummy node
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode fast = dummy;
        ListNode slow = dummy;

        // Step 2: Move fast pointer n steps ahead
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }

        // Step 3: Move both until fast reaches last node
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // Step 4: Delete the target node
        slow.next = slow.next.next;

        // Step 5: Return new head
        return dummy.next;
    }
}
