"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def fill_results(candidates, index, target, curr, results):
            if index >= len(candidates) and target > 0:
                return
            elif target == 0:
                results.add(tuple(curr))
                return
            elif target < 0:
                return
            elif target < candidates[index]:
                return
            fill_results(candidates, index + 1, target, curr, results)
            curr.append(candidates[index])
            fill_results(candidates, index + 1, target - candidates[index], curr, results)
            curr.pop()
                
                
            
        candidates.sort()
        curr = []
        results = set()
        fill_results(candidates, 0, target, curr, results)
        return list(results)
