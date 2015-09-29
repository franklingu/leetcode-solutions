/**
 * Given a list, rotate the list to the right by k places, where k is non-negative.
 * 
 * For example:
 * Given 1->2->3->4->5->NULL and k = 2,
 * return 4->5->1->2->3->NULL.
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
    public ListNode rotateRight(ListNode head, int k) {
        ListNode faster = head;
        ListNode slower = head;
        if (head == null) {
            return head;
        }
        int lengthOfList = 0;
        while (faster != null) {
            lengthOfList++;
            faster = faster.next;
        }
        faster = head;
        k = k % lengthOfList;
        for (int i = 0; i < k && faster != null; i++) {
            faster = faster.next;
        }
        if (faster == null || k == 0) {
            return head;
        }
        while (faster.next != null) {
            slower = slower.next;
            faster = faster.next;
        }
        ListNode newHead = slower.next;
        slower.next = null;
        faster.next = head;
        return newHead;
    }
}
