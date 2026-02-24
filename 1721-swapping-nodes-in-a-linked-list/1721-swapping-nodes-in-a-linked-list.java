class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        
        ListNode first = head;
        
        // Step 1: Move first to kth node from beginning
        for(int i = 1; i < k; i++) {
            first = first.next;
        }
        
        ListNode kthFromStart = first;
        
        // Step 2: Find kth node from end
        ListNode second = head;
        
        while(first.next != null) {
            first = first.next;
            second = second.next;
        }
        
        ListNode kthFromEnd = second;
        
        // Step 3: Swap values
        int temp = kthFromStart.val;
        kthFromStart.val = kthFromEnd.val;
        kthFromEnd.val = temp;
        
        return head;
    }
}