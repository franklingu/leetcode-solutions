'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import itertools

'''
Solution 1: using recursive approach
'''

class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if root.val == s:
                return [[root.val]]
        ll = self.pathSum(root.left, s - root.val)
        lr = self.pathSum(root.right, s - root.val)
        return [[root.val] + ls for ls in itertools.chain(ll, lr)]

'''
Solution 2: dfs
'''

class Solution2:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        if root is None:
            return []
        stk = [[root, [], s]]
        ps = []
        while stk:
            curr, p, s = stk.pop()
            if curr is None:
                continue
            np = p + [curr.val]
            if curr.left is None and curr.right is None:
                if curr.val == s:
                    ps.append(np)
                continue
            stk.append([curr.left, np, s - curr.val])
            stk.append([curr.right, np, s - curr.val])
        return ps
