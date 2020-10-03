"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n <= 0:
                nums[i] = 0
        for n in nums:
            i = abs(n) - 1
            if not (0 <= i < len(nums)):
                continue
            if nums[i] == 0:
                nums[i] = -inf
            elif nums[i] > 0:
                nums[i] = -nums[i]
        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1
        return len(nums) + 1
