"""

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
 
Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 
Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ss = sum(nums)
        if ss % 2 == 1:
            return False
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (ss // 2)  in possible_sums  