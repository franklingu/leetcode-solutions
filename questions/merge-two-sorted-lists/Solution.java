/**
 * Merge two sorted linked lists and return it as a new list. The new list should be made by
 * splicing together the nodes of the first two lists.
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null && l2 != null) {
            return l2;
        } else if (l1 != null && l2 == null) {
            return l1;
        }
        ListNode head, next1, next2, runner;
        if (l1.val < l2.val) {
            head = l1;
            next1 = l1.next;
            next2 = l2;
        } else {
            head = l2;
            next1 = l1;
            next2 = l2.next;
        }
        runner = head;
        
        while (next1 != null && next2 != null) {
            if (next1.val < next2.val) {
                runner.next = next1;
                next1 = next1.next;
            } else {
                runner.next = next2;
                next2 = next2.next;
            }
            runner = runner.next;
        }
        if (next1 == null) {
            runner.next = next2;
        } else {
            runner.next = next1;
        }
        
        return head;
    }
}
