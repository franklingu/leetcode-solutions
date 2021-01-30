"""

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any path.
 
Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

 
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def build_path_sum(node, mm):
            if node is None:
                return 0
            lm = build_path_sum(node.left, mm)
            rm = build_path_sum(node.right, mm)
            lm = lm if lm > 0 else 0
            rm = rm if rm > 0 else 0
            ss = lm + rm + node.val
            if mm[0] is None or mm[0] < ss:
                mm[0] = ss
            if lm > rm:
                ss = lm + node.val
            else:
                ss = rm + node.val
            return ss
        
        mm = [None]
        build_path_sum(root, mm)
        return mm[0]