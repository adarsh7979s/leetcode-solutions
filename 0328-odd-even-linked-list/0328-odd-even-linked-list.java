class Solution {
    public ListNode oddEvenList(ListNode head) {
        
        if(head == null || head.next == null) {
            return head;
        }
        
        ListNode odd = head;              // first node
        ListNode even = head.next;        // second node
        ListNode evenHead = even;         // store even list start
        
        while(even != null && even.next != null) {
            
            odd.next = even.next;         // connect odd to next odd
            odd = odd.next;               // move odd
            
            even.next = odd.next;         // connect even to next even
            even = even.next;             // move even
        }
        
        odd.next = evenHead;              // attach even list at end
        
        return head;
    }
}