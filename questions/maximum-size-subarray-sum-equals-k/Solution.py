"""

None
"""


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        mm = 0
        sums = {0: -1}
        curr = 0
        for i, n in enumerate(nums):
            curr += n
            if curr - k in sums:
                mm = max(mm, i - sums[curr - k])
            if curr not in sums:
                sums[curr] = i
        return mm