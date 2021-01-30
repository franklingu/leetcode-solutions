/**
 * Reverse a singly linked list.
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode prev = head, curr = head.next, temp = null, temp1;
        while (prev != null && curr != null) {
            prev.next = temp;
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
            temp = prev.next;
        }
        return prev;
    }
}
