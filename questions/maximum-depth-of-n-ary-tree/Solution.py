"""

Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
 
Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

 
Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 104].


"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        ml = 0
        for ch in root.children:
            ml = max(ml, self.maxDepth(ch))
        return ml + 1