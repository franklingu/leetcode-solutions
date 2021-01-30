'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ### method 1: can track start and end position
        # if not nums:
        #     return 0
        # start, end, max_sum, st = 0, 0, nums[0], 0
        # sum_sofar = nums[0]
        # for i, num in enumerate(nums):
        #     if i == 0:
        #         continue
        #     if sum_sofar < 0:
        #         sum_sofar = 0
        #         st = i
        #     sum_sofar += num
        #     if sum_sofar > max_sum:
        #         max_sum = sum_sofar
        #         start = st
        #         end = i
        # return max_sum
        ### method 2
        max_sum = None
        sum_sofar = 0
        for n in nums:
            sum_sofar += n
            if max_sum is None or max_sum < sum_sofar:
                max_sum = sum_sofar
            sum_sofar = max(0, sum_sofar)
        return max_sum
