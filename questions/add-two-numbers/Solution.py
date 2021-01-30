'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        new_head = None
        curr1, curr2 = l1, l2
        prev, curr = None, None
        while curr1 is not None or curr2 is not None:
            val1, val2 = 0, 0
            if curr1 is not None:
                val1 = curr1.val
                curr1 = curr1.next
            if curr2 is not None:
                val2 = curr2.val
                curr2 = curr2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            curr = ListNode(val)
            if prev is not None:
                prev.next = curr
            if new_head is None:
                new_head = curr
            prev = curr
        if carry > 0:
            curr = ListNode(carry)
            if prev:
                prev.next = curr
        return new_head
