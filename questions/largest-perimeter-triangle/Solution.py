"""

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
 
Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

 
Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106


"""


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(len(nums) - 1, -1, -1):
            if i > len(nums) - 3:
                continue
            elif i == len(nums) - 3:
                p1, p2 = nums[-1], nums[-2]
            if p1 < p2 + nums[i]:
                return nums[i] + p2 + p1
            p1, p2 = p2, nums[i]
        return s