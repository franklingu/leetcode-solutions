"""

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
 
Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false


Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true


Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false



 
Constraints:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def find_vals(node, x, y, lvl, pos1, pos2):
            if node.left is not None:
                if node.left.val == x:
                    pos1[0] = lvl + 1
                    pos1[1] = node
                if node.left.val == y:
                    pos2[0] = lvl + 1
                    pos2[1] = node
                find_vals(node.left, x, y, lvl + 1, pos1, pos2)
            if node.right is not None:
                if node.right.val == x:
                    pos1[0] = lvl + 1
                    pos1[1] = node
                if node.right.val == y:
                    pos2[0] = lvl + 1
                    pos2[1] = node
                find_vals(node.right, x, y, lvl + 1, pos1, pos2)
        
        if root is None:
            return False
        if root.val == x or root.val == y:
            return False
        pos1, pos2 = [-1, None], [-1, None]
        find_vals(root, x, y, 0, pos1, pos2)
        if pos1[0] == pos2[0] and pos1[0] != -1 and pos1[1] != pos2[1]:
            return True
        return False