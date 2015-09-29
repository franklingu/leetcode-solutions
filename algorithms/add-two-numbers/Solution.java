/**
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order
 * and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 * 
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumbersWithCarry(l1, l2, 0);
    }
    
    private ListNode addTwoNumbersWithCarry(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null) {
            if (carry == 0) {
                return null;
            } else {
                return new ListNode(carry);
            }
        }
        int num1 = (l1 == null) ? 0 : l1.val; 
        int num2 = (l2 == null) ? 0 : l2.val;
        ListNode next1 = (l1 == null) ? null : l1.next;
        ListNode next2 = (l2 == null) ? null : l2.next;
        int result = num1 + num2 + carry;
        carry = result / 10;
        result = result % 10;
        
        ListNode l = new ListNode(result);
        l.next = addTwoNumbersWithCarry(next1, next2, carry);
        return l;
    }
}
