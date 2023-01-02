"""

Given an integer array nums, return the number of all the arithmetic subsequences of nums.
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.

A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].

The test cases are generated so that the answer fits in 32-bit integer.
 
Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.

 
Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1


"""


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # use defaultdict(int) to easily get the difference in arithmetic subsequences ending with ```j```
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                
                # We are looking for the number of elements before j in the arithmetic subsequence that has nums[j]-nums[i] as difference.
                dif = nums[j]-nums[i]

                # Simply add it to the result.
                res += dp[j][dif]

                # Increase the number of elements in arithmetic subsequence at i with this dif.
                dp[i][dif] += dp[j][dif]+1
        return res