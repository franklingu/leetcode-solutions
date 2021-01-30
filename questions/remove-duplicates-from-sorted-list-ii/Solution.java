/**
 * Given a sorted linked list, delete all nodes that have duplicate numbers,
 * leaving only distinct numbers from the original list.
 *
 * For example,
 * Given 1->2->3->3->4->4->5, return 1->2->5.
 * Given 1->1->1->2->3, return 2->3.
 *
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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode nh = head, pprev = nh;
        ListNode prev = head;
        ListNode curr = head.next;

        while (prev != null && curr != null) {
            if (prev.val == curr.val) {
                while (curr != null && curr.val == prev.val) {
                    curr = curr.next;
                }
                if (prev == nh) {
                    nh = curr;
                    pprev = nh;
                    prev = curr;
                    if (curr == null) {
                        return nh;
                    } else {
                        curr = curr.next;
                    }
                } else {
                    pprev.next = curr;
                    prev = curr;
                    if (curr == null) {
                        return nh;
                    } else {
                        curr = curr.next;
                    }
                }
            } else {
                pprev = prev;
                prev = curr;
                curr = curr.next;
            }
        }

        return nh;
    }
}
