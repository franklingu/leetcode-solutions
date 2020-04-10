"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, ss: int) -> bool:
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return root.val == ss
        return self.hasPathSum(root.left, ss - root.val) or self.hasPathSum(root.right, ss - root.val)


class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def sums(node):
            if node is None:
                return set()
            if node.left is None and node.right is None:
                return set([node.val])
            ls = sums(node.left)
            rs = sums(node.right)
            ss = ls.union(rs)
            return set((t + node.val for t in ss))
        
        return sum in sums(root)
