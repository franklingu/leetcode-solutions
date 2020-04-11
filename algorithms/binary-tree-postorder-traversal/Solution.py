"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

"""
only iterative solution is presented. recursive solution is omitted
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stk = [(root, False, False)]
        ret = []
        while stk:
            curr, left_done, right_done = stk.pop()
            if curr is None:
                continue
            if left_done and right_done:
                ret.append(curr.val)
                continue
            elif left_done and not right_done:
                stk.append((curr, True, True))
                stk.append((curr.right, False, False))
            elif not left_done:
                stk.append((curr, True, False))
                stk.append((curr.left, False, False))
        return ret
