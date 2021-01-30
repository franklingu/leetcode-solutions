"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort_list(head):
            if head is None:
                return head
            elif head.next is None:
                return head
            elif head.next.next is None:
                if head.val > head.next.val:
                    tmp = head.next
                    head.next.next = head
                    head.next = None
                    head = tmp
                return head
            slow, fast = head, head
            while fast is not None:
                fast = fast.next
                if fast is None:
                    break
                fast = fast.next
                if fast is None:
                    break
                slow = slow.next
            tmp = slow.next
            slow.next = None
            c1 = sort_list(head)
            c2 = sort_list(tmp)
            curr = None
            head = None
            while c1 is not None or c2 is not None:
                if c1 is None:
                    if curr is not None:
                        curr.next = c2
                    curr = c2
                    c2 = c2.next
                elif c2 is None:
                    if curr is not None:
                        curr.next = c1
                    curr = c1
                    c1 = c1.next
                else:
                    if c1.val > c2.val:
                        if curr is not None:
                            curr.next = c2
                        curr = c2
                        c2 = c2.next
                    else:
                        if curr is not None:
                            curr.next = c1
                        curr = c1
                        c1 = c1.next
                if head is None:
                    head = curr
            return head
        
        return sort_list(head)
