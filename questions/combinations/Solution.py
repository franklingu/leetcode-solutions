"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def fill_results(index, n, curr, results):
            if len(curr) == k:
                results.append(list(curr))
                return
            elif index > n:
                return
            curr.append(index)
            fill_results(index + 1, n, curr, results)
            curr.pop()
            fill_results(index + 1, n, curr, results)
        
        results = []
        curr = []
        fill_results(1, n, curr, results)
        return results
