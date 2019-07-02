# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        nh = ListNode(None)
        prev, curr = nh, head
        while curr is not None:
            if curr.val == prev.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = curr
                curr = curr.next
                prev.next = None
        return nh.next
