"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def is_non_decreasing(ns):
            p = None
            for n in ns:
                if p is None:
                    p = n
                    continue
                if n < p:
                    return False
                p = n
            return True

        p = None
        for i, n in enumerate(nums):
            if p is None:
                p = n
                continue
            if n < p:
                ns1 = list(nums)
                ns1[i] = p
                ns2 = list(nums)
                ns2[i - 1] = n
                return is_non_decreasing(ns1) or is_non_decreasing(ns2)
            p = n
        return True

