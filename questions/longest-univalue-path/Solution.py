"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_longest(root, m):
            if root is None:
                return 0
            if root.left and root.left.val == root.val:
                c1 = find_longest(root.left, m)
            else:
                find_longest(root.left, m)
                c1 = 0
            if root.right and root.right.val == root.val:
                c2 = find_longest(root.right, m)
            else:
                find_longest(root.right, m)
                c2 = 0
            if m[0] < (c1 + c2):
                m[0] = c1 + c2
            return max(c1, c2) + 1

        m = [0]
        find_longest(root, m)
        return m[0]

