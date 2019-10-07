"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1, h2 = ListNode(None), ListNode(None)
        c1, c2 = h1, h2
        curr = head
        while curr is not None:
            if curr.val < x:
                c1.next = curr
                c1 = c1.next
            else:
                c2.next = curr
                c2 = c2.next
            # break the original next pointer
            # and move curr to next
            tmp = curr.next
            curr.next = None
            curr = tmp
        c1.next = h2.next
        return h1.next
