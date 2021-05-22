"""

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.
 
Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

 
Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109


"""


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        a, b = 0, 0
        if len(nums) % 2 == 0:
            a = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) // 2
            b = a + 1
        else:
            a = b = nums[len(nums) // 2]
        r1, r2 = 0, 0
        for n in nums:
            r1 += abs(n - a)
            r2 += abs(n - b)
        return min(r1, r2)