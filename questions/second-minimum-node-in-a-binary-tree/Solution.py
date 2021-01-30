"""
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def just_larger(node, m):
            if node is None:
                return -1
            if node.left is None:
                return node.val
            l = just_larger(node.left, m)
            r = just_larger(node.right, m)
            if l < 0 and r < 0:
                return node.val
            elif l < 0:
                return r
            elif r < 0:
                return l
            else:
                if l <= m:
                    return r
                if r <= m:
                    return l
                return min(l, r)

        if root is None:
            return -1
        m = root.val
        c = just_larger(root, m)
        if c <= m:
            return -1
        return c

