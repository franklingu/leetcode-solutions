"""

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
 
Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32

Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23

 
Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        if L <= root.val <= R:
            ss = root.val
        else:
            ss = 0
        return self.rangeSumBST(root.left, L, R) + ss + self.rangeSumBST(root.right, L, R)