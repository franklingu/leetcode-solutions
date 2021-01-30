"""

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]

 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10


"""


import collections


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ### method 1: with dict
#         def generate_subsets(candidates, index, counter, curr, subs):
#             if index >= len(candidates):
#                 subs.append(list(curr))
#                 return
#             candidate = candidates[index]
#             curr.extend([candidate] * counter[candidate])
#             for _ in range(counter[candidate]):
#                 generate_subsets(candidates, index + 1, counter, curr, subs)
#                 curr.pop()
#             generate_subsets(candidates, index + 1, counter, curr, subs)
        
#         counter = collections.Counter(nums)
#         candidates = sorted(list(counter.keys()))
#         subs = []
#         curr = []
#         generate_subsets(candidates, 0, counter, curr, subs)
#         return subs
        ### method 2
        ans = []
        nums.sort()
        self.backtrack(nums, ans, [], 0)
        return ans
    
    def backtrack(self, nums, ans, cur, start):
        ans.append(cur)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums, ans, cur + [nums[i]], i + 1)