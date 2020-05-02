"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse_ll(head):
            prev, curr, ne = None, head, head.next
            while curr is not None:
                curr.next = prev
                prev = curr
                curr = ne
                if ne:
                    ne = ne.next
            return prev
        
        if head is None or head.next is None:
            return True
        fast, slow = head, head
        while fast is not None:
            fast = fast.next
            if fast is None:
                break
            fast = fast.next
            if fast is None:
                break
            slow = slow.next
        second = slow.next
        slow.next = None
        new_head = reverse_ll(second)
        curr1, curr2 = head, new_head
        ret = True
        while curr1 is not None and curr2 is not None:
            if curr1.val != curr2.val:
                ret = False
                break
            curr1 = curr1.next
            curr2 = curr2.next
        slow.next = reverse_ll(new_head)
        return ret
