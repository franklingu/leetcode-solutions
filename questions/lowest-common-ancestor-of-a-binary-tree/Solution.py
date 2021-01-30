"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_lowest(curr, p, q):
            if curr is None:
                return None, False, False
            c1, p_found1, q_found1 = find_lowest(curr.left, p, q)
            c2, p_found2, q_found2 = find_lowest(curr.right, p, q)
            if c1 is not None or c2 is not None:
                return c1 if c2 is None else c2, True, True
            p_found = p_found1 or p_found2 or curr == p
            q_found = q_found1 or q_found2 or curr == q
            if p_found and q_found:
                return curr, p_found, q_found
            return None, p_found, q_found
        
        node, _, _ = find_lowest(root, p, q)
        return node
