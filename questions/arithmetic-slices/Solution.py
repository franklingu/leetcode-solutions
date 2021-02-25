"""

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.

Given an integer array nums, return the number of arithmetic subarrays of nums.
A subarray is a contiguous subsequence of the array.
 
Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:

Input: nums = [1]
Output: 0

 
Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000


"""


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ret = 0
        prev = None
        diff = None
        clen = 0
        for a in A:
            if prev is None:
                prev = a
                clen = 1
                continue
            if diff is None:
                diff = a - prev
                prev = a
                clen = 2
                continue
            if a - prev == diff:
                clen += 1
                prev = a
            else:
                if clen >= 3:
                    ret += (clen - 1) * (clen - 2) // 2
                diff = a - prev
                clen = 2
                prev = a
        if clen >= 3:
            ret += (clen - 1) * (clen - 2) // 2
        return ret
            