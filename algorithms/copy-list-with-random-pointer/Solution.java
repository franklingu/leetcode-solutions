/**
 * A linked list is given such that each node contains an additional random pointer which could point to any node
 * in the list or null.
 * 
 * Return a deep copy of the list.
 */

/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            return head;
        }
        RandomListNode curr = head;
        while (curr != null) {
            RandomListNode newNode = new RandomListNode(curr.label);
            newNode.next = curr.next;
            curr.next = newNode;
            curr = newNode.next;
        }
        curr = head;
        while (curr != null && curr.next != null) {
            if (curr.random == null) {
                curr.next.random = null;
            } else {
               curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }
        RandomListNode newHead = head.next;
        curr = head;
        RandomListNode newCurr = newHead;
        while (curr != null && newCurr != null) {
            curr.next = newCurr.next;
            curr = newCurr.next;
            if (curr != null) {
               newCurr.next = curr.next;
               newCurr = curr.next; 
            } else {
                newCurr.next = null;
            }
        }
        return newHead;
    }
}
