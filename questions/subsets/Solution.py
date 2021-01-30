"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate_subset(nums, ret, curr, index):
            if index >= len(nums):
                ret.append(list(curr))
                return
            generate_subset(nums, ret, curr, index + 1)
            curr.append(nums[index])
            generate_subset(nums, ret, curr, index + 1)
            curr.pop()
            
        ret = []
        curr = []
        generate_subset(nums, ret, curr, 0)
        return ret
