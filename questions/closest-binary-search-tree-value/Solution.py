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
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(node):
            if node is None:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
        
        diff, val = None, None
        for n in inorder(root):
            if diff is None or diff > abs(n - target):
                diff = abs(n - target)
                val = n
            if n > target:
                break
        return val