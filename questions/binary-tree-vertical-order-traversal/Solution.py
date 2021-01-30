"""

None
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        ### method 1: recursion, need to track h level
#         def build_vertical(node, vorder, horder, ret):
#             if node is None:
#                 return
#             if vorder not in ret:
#                 ret[vorder] = []
#             ret[vorder].append((horder, node.val))
#             build_vertical(node.left, vorder - 1, horder + 1, ret)
#             build_vertical(node.right, vorder + 1, horder + 1, ret)
        
#         ret = {}
#         build_vertical(root, 0, 0, ret)
#         return [[elem[1] for elem in sorted(ret[k], key=lambda x: x[0])] for k in sorted(ret.keys())]
        ### method 2: bfs
        import collections
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]