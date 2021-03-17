"""

You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.

Return the maximum binary tree built from nums.
 
Example 1:


Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.

Example 2:


Input: nums = [3,2,1]
Output: [3,null,2,null,1]

 
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
All integers in nums are unique.


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stk = []
        for n in nums:
            node = TreeNode(n)
            while stk and stk[-1].val < n:
                node.left = stk.pop()
            if stk:
                stk[-1].right = node
            stk.append(node)
        return stk[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def get_max_tree(nums, lo, hi, rank):
            if lo > hi:
                return None
            elif lo == hi:
                return TreeNode(val=nums[lo])
            node = None
            idx = -1
            for val, idx in rank:
                if lo <= idx <= hi:
                    node = TreeNode(val=val)
                    break
            left = get_max_tree(nums, lo, idx - 1, rank)
            right = get_max_tree(nums, idx + 1, hi, rank)
            node.left = left
            node.right = right
            return node
        
        rank = list(sorted([(val, idx) for idx, val in enumerate(nums)]))[::-1]
        return get_max_tree(nums, 0, len(nums) - 1, rank)