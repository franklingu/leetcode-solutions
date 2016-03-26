/**
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 *
 *
 * For example, the following two linked lists:
 *
 * A:          a1 → a2
 *                    ↘
 *                      c1 → c2 → c3
 *                    ↗
 * B:     b1 → b2 → b3
 * begin to intersect at node c1.
 *
 *
 * Notes:
 *
 * If the two linked lists have no intersection at all, return null.
 * The linked lists must retain their original structure after the function returns.
 * You may assume there are no cycles anywhere in the entire linked structure.
 * Your code should preferably run in O(n) time and use only O(1) memory.
 *
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int len1 = 0, len2 = 0, diff = 0, idx = 0;
        ListNode curr = headA, startA = null, startB = null;
        while (curr != null) {
            len1++;
            curr = curr.next;
        }
        curr = headB;
        while (curr != null) {
            len2++;
            curr = curr.next;
        }
        if (len1 > len2) {
            diff = len1 - len2;
            startA = headA;
            while (idx < diff) {
                startA = startA.next;
                idx++;
            }
            startB = headB;
        } else if (len1 < len2) {
            diff = len2 - len1;
            startB = headB;
            while (idx < diff) {
                startB = startB.next;
                idx++;
            }
            startA = headA;
        } else {
            startA = headA;
            startB = headB;
        }

        while (startA != null) {
            if (startA == startB) {
                return startA;
            }
            startA = startA.next;
            startB = startB.next;
        }
        return null;
    }
}
