"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def build_right_view(root, right, level):
            if root is None:
                return
            if len(right) <= level:
                right.append(None)
            right[level] = root.val
            build_right_view(root.left, right, level + 1)
            build_right_view(root.right, right, level + 1)
        
        right = []
        build_right_view(root, right, 0)
        return right


from collections import deque


class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            res.append(queue[0].val)
            for _ in range(size):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                
        return res
