"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid <= 0 or mid >= len(nums) - 1 or start == end - 1:
                break
            prev, curr, ne = nums[mid - 1], nums[mid], nums[mid + 1]
            if prev < curr and curr > ne:
                return mid
            elif curr > prev:
                start = mid
            elif curr > ne:
                end = mid
            else:
                end = mid
        return start if nums[start] > nums[end] else end
