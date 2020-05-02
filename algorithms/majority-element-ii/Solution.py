"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = None, None
        c1, c2 = 0, 0
        for n in nums:
            if n == num1:
                c1 += 1
            elif n == num2:
                c2 += 1
            elif c1 == 0:
                num1 = n
                c1 = 1
            elif c2 == 0:
                num2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0
        for n in nums:
            if n == num1:
                c1 += 1
            elif n == num2:
                c2 += 1
        ret = []
        if c1 > len(nums) // 3:
            ret.append(num1)
        if c2 > len(nums) // 3:
            ret.append(num2)
        return ret
