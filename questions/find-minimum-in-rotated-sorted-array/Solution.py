"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            if start == end - 1:
                return nums[start] if nums[start] < nums[end] else nums[end]
            mid = (start + end) // 2
            if nums[start] > nums[end]:
                if nums[mid] > nums[start]:
                    start = mid + 1
                else:
                    end = mid
            else:
                return nums[start]
        return nums[start]
