"""

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.
 
Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.


"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        nums.sort()
        track = [[1, i] for i, _ in enumerate(nums)]
        m, idx = 1, 0
        for i, e in enumerate(nums):
            j = i - 1
            while j >= 0:
                if e % nums[j] == 0 and track[i][0] < track[j][0] + 1:
                    track[i] = [track[j][0] + 1, j]
                j -= 1
            if track[i][0] > m:
                m = track[i][0]
                idx = i
        ss = []
        while idx >= 0:
            ss.append(nums[idx])
            idx2 = track[idx][1]
            if idx2 == idx:
                break
            idx = idx2
        ss.sort()
        return ss