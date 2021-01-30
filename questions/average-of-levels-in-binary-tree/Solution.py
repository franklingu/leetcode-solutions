"""

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].


Note:

The range of node's value is in the range of 32-bit signed integer.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def get_nodes_in_levels(node, level, levels):
            if node is None:
                return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(node.val)
            get_nodes_in_levels(node.left, level + 1, levels)
            get_nodes_in_levels(node.right, level + 1, levels)
        
        def get_averages(levels):
            return [float(sum(level)) / len(level) for level in levels]
        
        levels = []
        get_nodes_in_levels(root, 0, levels)
        return get_averages(levels)