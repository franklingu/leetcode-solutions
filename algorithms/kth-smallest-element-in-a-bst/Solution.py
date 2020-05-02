"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder2(node, k):
            stack = [node]
            visited = set()
            while stack:
                curr = stack[-1]
                while curr.left is not None and curr.left not in visited:
                    stack.append(curr.left)
                    curr = curr.left
                curr = stack.pop()
                visited.add(curr)
                if k == 1:
                    return curr.val
                k -= 1
                if curr.right is not None:
                    stack.append(curr.right)
            return None

        return inorder2(root, k)



class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node is None:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        for i, val in enumerate(inorder(root)):
            if i == k - 1:
                return val
        return None
