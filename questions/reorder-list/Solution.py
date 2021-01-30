"""

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse_list(node):
            prev, curr = None, node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        if slow is None or slow.next is None:
            return
        half = slow.next
        slow.next = None
        curr2 = reverse_list(half)
        curr1 = head.next
        curr = head
        while curr1 is not None or curr2 is not None:
            if curr2 is not None:
                curr.next = curr2
                curr2 = curr2.next
                curr = curr.next
            if curr1 is not None:
                curr.next = curr1
                curr1 = curr1.next
                curr = curr.next