'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, n in enumerate(nums):
            if n not in track:
                track[n] = [i]
            else:
                track[n].append(i)
        for k in track:
            left = target - k
            if left not in track:
                continue
            if left == k and len(track[k]) == 1:
                continue
            elif left == k:
                return track[k]
            return [track[k][0], track[left][0]]
