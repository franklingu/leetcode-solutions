"""

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.
 
Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

 
Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100


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