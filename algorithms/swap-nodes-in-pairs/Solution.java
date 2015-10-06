/**
 * Given a linked list, swap every two adjacent nodes and return its head.
 * 
 * For example,
 *   Given 1->2->3->4, you should return the list as 2->1->4->3.
 *   Your algorithm should use only constant space. You may not modify the values in the list,
 *   only nodes itself can be changed.
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
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode first = head.next;
        ListNode temp = first.next;
        head.next = temp;
        first.next = head;
        ListNode prev = first;
        ListNode curr = first.next;
        int num = 1;
        while (prev != null && curr != null) {
            if (num % 2 == 0) {
                if (curr.next != null) {
                    temp = curr.next;
                    curr.next = temp.next;
                    temp.next = curr;
                    prev.next = temp;
                    curr = temp;
                } else {
                    break;
                }
            }
            prev = prev.next;
            curr = curr.next;
            num++;
        }
        
        return first;
    }
}
