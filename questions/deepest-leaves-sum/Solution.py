"""

Given a binary tree, return the sum of values of its deepest leaves.
 
Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

 
Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        stk = [root]
        while True:
            ne = []
            for node in stk:
                if node.left is not None:
                    ne.append(node.left)
                if node.right is not None:
                    ne.append(node.right)
            if not ne:
                break
            stk = ne
        return sum([n.val for n in stk])