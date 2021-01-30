"""

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
Notice that the solution set must not contain duplicate quadruplets.
 
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:
Input: nums = [], target = 0
Output: []

 
Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109


"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ss = dict()
        results = set()
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if j <= i:
                    continue
                s = n1 + n2
                for idx1, idx2 in ss.get(target - s, set()):
                    if not (i != idx1 and i != idx2 and j != idx1 and j != idx2):
                        continue
                    elem = tuple(sorted((nums[idx1], nums[idx2], nums[i], nums[j])))
                    results.add(elem)
                ss[s] = ss.get(s, []) + [(i, j)]
        return [list(el) for el in results]