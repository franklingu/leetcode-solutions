"""

None
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if len(s) == 0:
            return None
        is_negative = False
        curr = 0
        cnt = 0
        ls, le, rs, re = -1, -1, -1, -1
        for i, c in enumerate(s):
            if c == '(':
                cnt += 1
                if cnt == 1:
                    if ls == -1:
                        ls = i
                    else:
                        rs = i
            elif c == ')':
                cnt -= 1
                if cnt == 0:
                    if le == -1:
                        le = i
                    else:
                        re = i
            else:
                if cnt == 0:
                    if c == '-':
                        is_negative = True
                    else:
                        curr = curr * 10 + ord(c) - ord('0')
        node = TreeNode(curr if not is_negative else -curr)
        if ls != -1:
            node.left = self.str2tree(s[ls + 1:le])
        if rs != -1:
            node.right = self.str2tree(s[rs + 1:re])
        return node