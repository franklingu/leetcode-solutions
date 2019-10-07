"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:            
        nh = ListNode(None)
        np, nc = None, nh
        curr = head
        should_retreat = False
        while curr is not None:
            if curr.val == nc.val:
                should_retreat = True
            else:
                if should_retreat:
                    np.next = curr
                    nc = curr
                else:
                    nc.next = curr
                    np = nc
                    nc = curr
                should_retreat = False
            curr = curr.next
        if should_retreat:
            np.next = None
        return nh.next
