"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def construct(preorder, idx, inorder, start, end):
            if start > end:
                return None
            node = TreeNode(preorder[idx])
            i = inorder[start:end + 1].index(preorder[idx]) + start
            left = construct(preorder, idx + 1, inorder, start, i - 1)
            right = construct(preorder, idx + 1 + i - start, inorder, i + 1, end)
            node.left = left
            node.right = right
            return node
            
        return construct(preorder, 0, inorder, 0, len(inorder) - 1)
