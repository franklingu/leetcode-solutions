"""

None
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def isValid(root, arr, idx):
            if root is None:
                return False
            if len(arr) == idx:
                return False
            if root.val != arr[idx]:
                return False
            if root.left is None and root.right is None:
                return len(arr) == idx + 1
            if len(arr) == idx + 1:
                return False
            lr = rr = False
            if root.left is not None and root.left.val == arr[idx + 1]:
                lr = isValid(root.left, arr, idx + 1)
            if root.right is not None and root.right.val == arr[idx + 1]:
                rr = isValid(root.right, arr, idx + 1)
            return lr or rr
            
        return isValid(root, arr, 0)
        