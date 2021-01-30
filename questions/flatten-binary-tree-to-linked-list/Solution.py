"""

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

 
Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]

 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

 
Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_to_list(node):
            if node is None:
                return None, None
            lh, lt = flatten_to_list(node.left)
            rh, rt = flatten_to_list(node.right)
            node.left = None
            node.right = lh
            if lt is not None:
                lt.left = None
                lt.right = rh
            else:
                lt = node
                lt.right = rh
                lt.left = None
            if rt is not None:
                rt.left = None
                rt.right = None
            else:
                rt = lt
            return node, rt
            
        flatten_to_list(root)