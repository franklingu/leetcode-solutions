/**
 * Given a singly linked list, determine if it is a palindrome.
 *
 * Follow up:
 * Could you do it in O(n) time and O(1) space?
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
    public boolean isPalindrome(ListNode head) {
        if (head == null) {
            return true;
        } else if (head.next == null) {
            return true;
        }
        ListNode slower = head, faster = head;
        while (faster != null && faster.next != null) {
            slower = slower.next;
            faster = faster.next.next;
        }
        ListNode lower = slower, prev = null, curr = head, tmp = null;
        if (faster != null) {
            lower = slower.next;
        }
        while (curr != slower) {
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        ListNode upper = prev;
        boolean result = true;
        while (upper != null && lower != null) {
            if (upper.val != lower.val) {
                result = false;
                break;
            }
            upper = upper.next;
            lower = lower.next;
        }
        tmp = curr;
        curr = prev;
        prev = tmp;
        while (curr != null) {
            tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }
        return result;
    }
}
