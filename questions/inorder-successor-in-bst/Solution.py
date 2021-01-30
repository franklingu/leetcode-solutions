"""

None
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inorder(node):
            if node is None:
                return
            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)
        
        prev = None
        for n in inorder(root):
            if prev is None:
                prev = n
                continue
            if prev == p:
                return n
            prev = n
        return None