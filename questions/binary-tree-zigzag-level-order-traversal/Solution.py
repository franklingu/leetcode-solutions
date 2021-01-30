"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def level_order(node, levels, curr):
            if node is None:
                return
            if len(levels) <= curr:
                levels.append([])
            levels[curr].append(node.val)
            level_order(node.left, levels, curr + 1)
            level_order(node.right, levels, curr + 1)
        
        def zigzag(levels):
            ret = []
            for i, level in enumerate(levels):
                if i % 2 == 1:
                    ret.append(level[::-1])
                else:
                    ret.append(level)
            return ret
        
        levels = []
        level_order(root, levels, 0)
        return zigzag(levels)