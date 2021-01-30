"""

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
 
Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

 
Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

 
Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        curr, next_head, next_curr = root, None, None
        while curr is not None:
            if next_curr is None:
                if curr.left is not None:
                    next_curr = curr.left
                    next_head = next_curr
                    if curr.right is not None:
                        curr.left.next = curr.right
                        next_curr = curr.right
                elif curr.right is not None:
                    next_curr = curr.right
                    next_head = next_curr
            else:
                if curr.left is not None:
                    next_curr.next = curr.left
                    next_curr = curr.left
                    if curr.right is not None:
                        curr.left.next = curr.right
                        next_curr = curr.right
                elif curr.right is not None:
                    next_curr.next = curr.right
                    next_curr = curr.right
            if curr.next is not None:
                curr = curr.next
            else:
                curr = next_head
                next_head, next_curr = None, None
        return root
            