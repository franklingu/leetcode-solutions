/**
 * Remove all elements from a linked list of integers that have value val.
 * 
 * Example
 * Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
 * Return: 1 --> 2 --> 3 --> 4 --> 5
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
    public ListNode removeElements(ListNode head, int val) {
        if (head == null) {
            return head;
        }
        boolean isHead = true;
        ListNode curr = head, first = head, prev = null, temp = null;
        while (curr != null) {
            if (isHead) {
                if (curr.val == val) {
                    temp = curr.next;
                    curr.next = null;
                    curr = temp;
                    first = curr;
                } else {
                    isHead = false;
                    prev = curr;
                    first = curr;
                    curr = curr.next;
                }
                continue;
            } else {
                if (curr.val == val) {
                    prev.next = curr.next;
                    curr.next = null;
                    curr = prev.next;
                } else {
                    prev = curr;
                    curr = curr.next;
                }
            }
        }
        return first;
    }
}
