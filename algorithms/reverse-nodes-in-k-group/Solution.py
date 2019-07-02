'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

'''
For every k nodes, break it from the original list, reverse it and
then add the part back. If fewer than k remaining, do nothing.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(node):
            prev, curr = None, node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev, node
        
        def getKNodes(node, k):
            curr = node
            while k > 1 and curr is not None:
                k -= 1
                curr = curr.next
            if curr is None:
                return False, curr
            return True, curr
        
        if k < 2:
            return head
        nh = ListNode(None)
        nh.next = head
        curr = nh
        while curr is not None:
            part_head = curr.next
            can_take, part_tail = getKNodes(part_head, k)
            if not can_take:
                break
            next_head = part_tail.next
            part_tail.next = None
            rh, rt = reverseLinkedList(part_head)
            curr.next = rh
            curr = rt
            curr.next = next_head
        return nh.next
