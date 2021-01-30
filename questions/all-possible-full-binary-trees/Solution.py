"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.



 Example 1:

 Input: 7
 Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
 Explanation:

  ![Image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png)

  Note:

  1 <= N <= 20
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        if N % 2 != 1 or N < 0:
            return []
        ret = []
        for i in xrange(0, N - 1, 2):
            l = i + 1
            r = N - l - 1
            ls = self.allPossibleFBT(l)
            rs = self.allPossibleFBT(r)
            for lt in ls:
                for rt in rs:
                    root = TreeNode(0)
                    root.left = lt
                    root.right = rt
                    ret.append(root)
        return ret

