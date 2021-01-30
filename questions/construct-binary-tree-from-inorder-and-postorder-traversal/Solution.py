"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        node = TreeNode(postorder[-1])
        idx = 0
        for i, val in enumerate(inorder):
            if val == postorder[-1]:
                idx = i
                break
        left = self.buildTree(inorder[0:idx], postorder[0:idx])
        right = self.buildTree(inorder[idx + 1:], postorder[idx:len(postorder) - 1])
        node.left = left
        node.right = right
        return node
