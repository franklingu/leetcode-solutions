"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_money(nums, index, track, tail_taken):
            if index < 0:
                return 0
            elif index == 0:
                if tail_taken:
                    return 0
                else:
                    return nums[index]
            if (index, tail_taken) in track:
                return track[(index, tail_taken)]
            m1 = get_money(nums, index - 2, track, tail_taken) + nums[index]
            m2 = get_money(nums, index - 1, track, tail_taken)
            ret = max(m1, m2)
            track[(index, tail_taken)] = ret
            return ret
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        track = {}
        m1 = get_money(nums, len(nums) - 1, track, True)
        m2 = get_money(nums, len(nums) - 2, track, False)
        return max(m1, m2)
