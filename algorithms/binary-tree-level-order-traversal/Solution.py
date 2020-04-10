"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def build_levels(node, levels, level):
            if node is None:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            build_levels(node.left, levels, level + 1)
            build_levels(node.right, levels, level + 1)
            
        levels = []
        build_levels(root, levels, 0)
        return levels
