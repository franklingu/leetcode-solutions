"""

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
 
Example 1:
Input: nums = [1,2,3]
Output: 6
Example 2:
Input: nums = [1,2,3,4]
Output: 24
Example 3:
Input: nums = [-1,-2,-3]
Output: -6

 
Constraints:

3 <= nums.length <= 104
-1000 <= nums[i] <= 1000


"""


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        positive = sorted([n for n in nums if n >= 0])
        negative = sorted([n for n in nums if n < 0])
        cs1 = positive[-3:]
        cs2 = negative[:2]
        if len(cs1) < 3:
            return cs2[1] * cs2[0] * cs1[-1]
        m = cs1[1] * cs1[0] * cs1[2]
        if len(cs2) == 2:
            m = max(cs2[1] * cs2[0] * cs1[2], m)
        return m