"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mlen = len(nums) + 1
        start = 0
        ss = 0
        for i, n in enumerate(nums):
            ss += n
            while ss >= s:
                mlen = min(i - start + 1, mlen)
                ss -= nums[start]
                start += 1
        return mlen if mlen != len(nums) + 1 else 0
