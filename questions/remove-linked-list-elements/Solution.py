"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        nh = ListNode(None)
        nh.next = head
        prev, curr = nh, head
        while curr is not None:
            n = curr.next
            if curr.val == val:
                prev.next = n
                curr = n
            else:
                prev = curr
                curr = n
        return nh.next
