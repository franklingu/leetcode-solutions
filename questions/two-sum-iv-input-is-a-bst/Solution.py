"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(root, nums):
            if root is None:
                return
            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)

        nums = []
        inorder(root, nums)
        track = {}
        for n in nums:
            if n not in track:
                track[n] = 0
            track[n] += 1
        for n in nums:
            t = k - n
            if t != n and t in track:
                return True
            if t == n and track[t] > 1:
                return True
        return False

