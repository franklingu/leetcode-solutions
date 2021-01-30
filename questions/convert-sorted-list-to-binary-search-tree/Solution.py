"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        prev = None
        slow, fast = head, head
        while fast is not None:
            fast = fast.next
            if fast is not None:
                prev = slow
                slow = slow.next
            else:
                break
            fast = fast.next
        if prev is None:
            if head is None:
                return None
            node = TreeNode(head.val)
            return node
        prev.next = None
        nn = slow.next
        slow.next = None
        node = TreeNode(slow.val)
        left = self.sortedListToBST(head)
        right = self.sortedListToBST(nn)
        node.left = left
        node.right = right
        return node
