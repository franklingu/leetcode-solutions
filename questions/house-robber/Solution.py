"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_money(nums, index, track):
            if index < 0:
                return 0
            if index in track:
                return track[index]
            m1 = get_money(nums, index - 2, track) + nums[index]
            m2 = get_money(nums, index - 3, track) + nums[index]
            m3 = get_money(nums, index - 1, track)
            ret = max(m1, m2, m3)
            track[index] = ret
            return ret
        
        track = {}
        return get_money(nums, len(nums) - 1, track)
