/**
 * Reverse a linked list from position m to n. Do it in-place and in one-pass.
 *
 *For example:
 *Given 1->2->3->4->5->NULL, m = 2 and n = 4,
 *
 *return 1->4->3->2->5->NULL.
 *
 *Note:
 *Given m, n satisfy the following condition:
 *1 ≤ m ≤ n ≤ length of list.
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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n) {
            return head;
        }
        ListNode start = null, end = null, curr = head;
        ListNode prev = null, prevMark = null, tmp = null;
        int idx = 1;
        while (curr != null) {
            if (idx == m - 1) {
                prevMark = curr;
            }
            if (idx == m) {
                start = curr;
            }
            if (idx == n) {
                end = curr.next;
                break;
            }
            curr = curr.next;
            idx++;
        }
        curr = start;
        prev = end;
        while (curr != end) {
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        if (prevMark != null) {
            prevMark.next = prev;
        } else {
            head = prev;
        }
        return head;
    }
}
