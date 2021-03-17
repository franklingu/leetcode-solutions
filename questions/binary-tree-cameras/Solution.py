"""

Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.
 
Example 1:



Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.


Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.


Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.




"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        ret = [0]
        
        def install_cams(node):
            if node is None:
                return True, False
            elif node.left is None and node.right is None:
                return False, False
            ld, li = install_cams(node.left)
            rd, ri = install_cams(node.right)
            if not ld or not rd:
                ret[0] = ret[0] + 1
                return True, True
            if li or ri:
                return True, False
            return False, False
            
            
        rd, ri = install_cams(root)
        if not rd:
            ret[0] += 1
        return ret[0]