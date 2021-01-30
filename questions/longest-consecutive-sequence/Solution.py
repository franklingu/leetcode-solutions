"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 
Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109

 
Follow up: Could you implement the O(n) solution?
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ms = 0
        track = {}
        for n in nums:
            if n in track:
                continue
            if n - 1 in track and n + 1 in  track:
                track[n] = track[n - 1] + track[n + 1] + 1
                track[n - track[n - 1]] = track[n]
                track[n + track[n + 1]] = track[n]
            elif n - 1 in track:
                track[n] = track[n - 1] + 1
                track[n - track[n - 1]] = track[n]
            elif n + 1 in track:
                track[n] = track[n + 1] + 1
                track[n + track[n + 1]] = track[n]
            else:
                track[n] = 1
            ms = max(ms, track[n])
        return ms