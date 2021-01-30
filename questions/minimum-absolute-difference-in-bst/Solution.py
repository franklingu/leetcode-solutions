"""

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

 
Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_maxmin(root, m):
            if root is None:
                return None, None
            lefts = get_maxmin(root.left, m)
            rights = get_maxmin(root.right, m)
            if root.left is None and root.right is None:
                return root.val, root.val
            elif root.left is None and root.right is not None:
                if m[0] is None or m[0] > rights[0] - root.val:
                    m[0] = rights[0] - root.val
                return root.val, rights[1]
            elif root.right is None and root.left is not None:
                if m[0] is None or m[0] > root.val - lefts[1]:
                    m[0] = root.val - lefts[1]
                return lefts[0], root.val
            else:
                if m[0] is None or m[0] > rights[0] - root.val:
                    m[0] = rights[0] - root.val
                if m[0] is None or m[0] > root.val - lefts[1]:
                    m[0] = root.val - lefts[1]
                return lefts[0], rights[1]
        
        m = [None]
        get_maxmin(root, m)
        return m[0]