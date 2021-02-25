"""

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.
Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
 
Example 1:


Input: root = [4,2,6,1,3]
Output: 1

Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

 
Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder(node):
            if node.left is not None:
                yield from inorder(node.left)
            yield node.val
            if node.right is not None:
                yield from inorder(node.right)
        d = float('inf')
        prev = None
        for n in inorder(root):
            if prev is None:
                prev = n
                continue
            d = min(d, n - prev)
            prev = n
        return d