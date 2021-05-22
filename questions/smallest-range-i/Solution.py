"""
Given an array nums of integers, for each integer nums[i] we may choose any x with -k <= x <= k, and add x to nums[i].

After this process, we have some array result.

Return the smallest possible difference between the maximum value of result and the minimum value of result.

 

Example 1:

Input: nums = [1], k = 0
Output: 0
Explanation: result = [1]
Example 2:

Input: nums = [0,10], k = 2
Output: 6
Explanation: result = [2,8]
Example 3:

Input: nums = [1,3,6], k = 3
Output: 0
Explanation: result = [3,3,3] or result = [4,4,4]
 

Note:

1 <= nums.length <= 10000
0 <= nums[i] <= 10000
0 <= k <= 10000
"""

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if K == 0:
            return max(A) - min(A)
        r = max(A) - min(A) - K * 2
        return r if r > 0 else 0