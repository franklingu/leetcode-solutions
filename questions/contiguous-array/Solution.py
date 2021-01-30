"""

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.


Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Note:
The length of the given binary array will not exceed 50,000.

"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        track = {0: [-1]}
        ss = 0
        ms = 0
        for i, n in enumerate(nums):
            if n == 0:
                ss -= 1
            else:
                ss += 1
            ts = 0
            if ss not in track:
                track[ss] = [i]
            elif len(track[ss]) == 1:
                track[ss].append(i)
                ts = i - track[ss][0]
            else:
                track[ss][1] = i
                ts = i - track[ss][0]
            ms = max(ms, ts)
        return ms
