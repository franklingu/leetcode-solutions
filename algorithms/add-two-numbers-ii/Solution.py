'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

'''
Reverse linked list and then add. Finally return the reversed result.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(node):
            prev, curr = None, node
            while curr is not None:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        def addLists(n1, n2):
            nh = ListNode(None)
            curr = nh
            carry = 0
            while n1 is not None or n2 is not None:
                val = carry
                if n1 is not None:
                    val += n1.val
                    n1 = n1.next
                if n2 is not None:
                    val += n2.val
                    n2 = n2.next
                carry, val = divmod(val, 10)
                node = ListNode(val)
                curr.next = node
                curr = node
            if carry > 0:
                node = ListNode(carry)
                curr.next = node
                curr = node
            return nh.next
            
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        nh = reverseList(addLists(l1, l2))
        return nh
