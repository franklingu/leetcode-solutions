/**
 * Given a linked list, remove the nth node from the end of list and return its head.
 * 
 * For example,
 * 
 *   Given linked list: 1->2->3->4->5, and n = 2.
 * 
 *   After removing the second node from the end, the linked list becomes 1->2->3->5.
 * Note:
 * Given n will always be valid.
 * Try to do this in one pass.
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return null;
        }
        ListNode faster = head.next;
        ListNode prev = head;
        while ((--n) > 0 && faster != null) {
            faster = faster.next;
        }
        if (faster == null) {
            ListNode temp = head.next;
            head.next = null;
            return temp;
        }
        while (faster.next != null) {
            faster = faster.next;
            prev = prev.next;
        }
        ListNode temp = prev.next.next;
        prev.next.next = null;
        prev.next = temp;
        return head;
    }
}
