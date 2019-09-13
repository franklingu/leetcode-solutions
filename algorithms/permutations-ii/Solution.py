'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(candidates, curr, perms):
            if sum(candidates.values()) == 0:
                perms.append(list(curr))
                return
            for n in list(candidates.keys()):
                if candidates[n] == 0:
                    continue
                curr.append(n)
                candidates[n] -= 1
                generate_permutations(candidates, curr, perms)
                curr.pop()
                candidates[n] += 1
            
        curr = []
        candidates = Counter(nums)
        perms = []
        generate_permutations(candidates, curr, perms)
        return perms
