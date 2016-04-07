/**
 * Given a singly linked list, group all odd nodes together followed by the even nodes.
 * Please note here we are talking about the node number and not the value in the nodes.
 * 
 * You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
 * 
 * Example:
 * Given 1->2->3->4->5->NULL,
 * return 1->3->5->2->4->NULL.
 * 
 * Note:
 * The relative order inside both the even and odd groups should remain as it was in the input. 
 * The first node is considered odd, the second node even and so on ...
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
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode curr = head.next.next;
        ListNode oddHead = head, evenHead = head.next, oddTail = oddHead, evenTail = evenHead;
        while (curr != null) {
            oddTail.next = curr;
            oddTail = curr;
            if (curr.next == null) {
                curr = curr.next;
            } else {
                evenTail.next = curr.next;
                evenTail = curr.next;
                curr = curr.next.next;
            }
        }
        oddTail.next = evenHead;
        evenTail.next = null;
        
        return head;
    }
}
