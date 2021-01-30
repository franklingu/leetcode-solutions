"""

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

 
For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2

 
return [2].
Note: If a tree has more than one mode, you can return them in any order.
Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def track(root, tr):
            if root is None:
                return
            if root.val not in tr:
                tr[root.val] = 0
            tr[root.val] += 1
            track(root.left, tr)
            track(root.right, tr)
        
        tr = {}
        track(root, tr)
        m = None
        r = []
        for v, c in tr.iteritems():
            if m is None or c > m:
                m = c
                r = [v]
            elif c == m:
                r.append(v)
        return r