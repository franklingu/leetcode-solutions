'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i - 1]:
                continue
            target = -n
            start, end = i + 1, len(nums) - 1
            while start < end:
                s = nums[start] + nums[end]
                if s < target:
                    start += 1
                elif s > target:
                    end -= 1
                else:
                    ret.append([n, nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
        return ret
