"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ### method 1: track positive and negative separately
        max_prod = None
        positive, negative = 1, 1
        for n in nums:
            t1, t2 = positive, negative
            positive = max(t1 * n, t2 * n)
            negative = min(t1 * n, t2 * n)
            if max_prod is None or max_prod < positive:
                max_prod = positive
            if max_prod is None or max_prod < negative:
                max_prod = negative
            if positive <= 0:
                positive = 1
            if negative >= 0:
                negative = 1
        return max_prod


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        # method 2: track max and min only, try to handle positive and negative together
        if not nums:
            return 0
        imax = imin = 1
        tmax = None
        for n in nums:
            t1, t2 = imax, imin
            imax = max(t1 * n, t2 * n, n)
            imin = min(t1 * n, t2 * n, n)
            if tmax is None or tmax < imax:
                tmax = imax
        return tmax
