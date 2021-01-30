"""

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        ### method 1: dp
#         def get_money(node, track):
#             if node is None:
#                 return 0
#             if node in track:
#                 return track[node]
#             val = node.val
#             if node.left is not None:
#                 val += get_money(node.left.left, track) + get_money(node.left.right, track)
#             if node.right is not None:
#                 val += get_money(node.right.left, track) + get_money(node.right.right, track)
#             m2 = get_money(node.left, track) + get_money(node.right, track)
#             track[node] = max(val, m2)
#             return track[node]
        
#         track = {}
#         ret = get_money(root, track)
#         return ret
        ### method 2: dfs
        def dfs(node):
            if node is None:
                return (0, 0)
            l_robbed, l_not_robbed = dfs(node.left)
            r_robbed, r_not_robbed = dfs(node.right)
            ret = node.val + l_not_robbed + r_not_robbed, max(l_robbed + r_robbed, l_not_robbed + r_not_robbed, l_robbed + r_not_robbed, l_not_robbed + r_robbed)
            return ret
        
        return max(dfs(root))