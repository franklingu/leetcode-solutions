"""

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.
 
Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]

 
Constraints:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.


"""


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def generate(nums, idx, curr, ret):
            if len(curr) >= 2:
                ret.append(tuple(curr))
            if idx > len(nums):
                return
            ss = set()
            for i in range(idx, len(nums)):
                if curr and curr[-1] > nums[i]:
                    continue
                if nums[i] in ss:
                    continue
                ss.add(nums[i])
                curr.append(nums[i])
                generate(nums, i + 1, curr, ret)
                curr.pop()
        
        ret = []
        generate(nums, 0, [], ret)
        return [list(e) for e in ret]