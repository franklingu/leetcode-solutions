"""

You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
 
Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:

Input: head = [1], k = 1
Output: [1]

Example 4:

Input: head = [1,2], k = 1
Output: [2,1]

Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]

 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def get_k_from_head(h, k):
            p, c = h, h.next
            while k > 1:
                p = c
                c = c.next
                k -= 1
            return p, c
        
        def get_k_from_tail(h, k):
            f = h.next
            while k > 0:
                f = f.next
                k -= 1
            p, c = h, h.next
            while f is not None:
                p = c
                c = c.next
                f = f.next
            return p, c
            
        
        if head is None or head.next is None:
            return head
        nh = ListNode()
        nh.next = head
        p1, c1 = get_k_from_head(nh, k)
        p2, c2 = get_k_from_tail(nh, k)
        if c1 == c2:
            return nh.next
        if p1 == c2:
            p2.next = c1
            c1_next = c1.next
            c1.next = c2
            c2.next = c1_next
            return nh.next
        if p2 == c1:
            p1.next = c2
            c2_next = c2.next
            c2.next = c1
            c1.next = c2_next
            return nh.next
        c2_next = c2.next
        c2.next = c1.next
        c1.next = c2_next
        p1.next = c2
        p2.next = c1
        return nh.next