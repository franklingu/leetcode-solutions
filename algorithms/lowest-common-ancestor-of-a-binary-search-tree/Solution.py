"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

![img](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findLCA(node, p, q):
            if node is None:
                return None, False, False
            c_p = node == p
            c_q = node == q
            l_f, l_p, l_q = findLCA(node.left, p, q)
            r_f, r_p, r_q = findLCA(node.right, p, q)
            if l_f is not None:
                return l_f, True, True
            if r_f is not None:
                return r_f, True, True
            if (l_p or r_p or c_p) and (l_q or r_q or c_q):
                return node, True, True
            return None, (l_p or r_p or c_p), (l_q or r_q or c_q)
        
        ret = findLCA(root, p, q)
        return ret[0]
        
