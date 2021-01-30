"""

None
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        lh = self.treeToDoublyList(root.left)
        rh = self.treeToDoublyList(root.right)
        lt, rt = None, None
        if lh is None:
            lh = lt = root
        else:
            lt = lh.left
            lt.right = root
            root.left = lt
        if rh is None:
            root.right = None
            rh = rt = root
        else:
            rt = rh.left
            rh.left = root
            root.right = rh
        lh.left = rt
        rt.right = lh
        return lh