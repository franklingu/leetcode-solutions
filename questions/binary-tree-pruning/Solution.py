"""

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.
 
Example 1:


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Example 2:


Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:


Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

 
Constraints:

The number of nodes in the tree is in the range [1, 200].
Node.val is either 0 or 1.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def only_zeros(node):
            if node is None:
                return True
            l = only_zeros(node.left)
            r = only_zeros(node.right)
            c = node.val == 0
            if l and r and c:
                return True
            if l:
                node.left = None
            if r:
                node.right = None
            return False
        
        ret = only_zeros(root)
        if ret:
            return None
        return root