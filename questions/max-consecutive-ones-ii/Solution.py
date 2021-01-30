"""

None
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mmax = 0
        start = 0
        zeros = 0
        for i, n in enumerate(nums):
            if n == 1:
                mmax = max(mmax, i - start + 1)
            else:
                zeros += 1
                while zeros > 1:
                    if nums[start] == 0:
                        zeros -= 1
                    start += 1
                mmax = max(mmax, i - start + 1)
        return max(mmax, len(nums) - start)