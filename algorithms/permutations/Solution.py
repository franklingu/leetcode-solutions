'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutation(nums, ret, curr, visited):
            if len(curr) == len(nums):
                ret.append(list(curr))
                return
            for num in nums:
                if num in visited:
                    continue
                visited.add(num)
                curr.append(num)
                generate_permutation(nums, ret, curr, visited)
                curr.pop()
                visited.remove(num)
            
        ret = []
        curr = []
        visited = set()
        generate_permutation(nums, ret, curr, visited)
        return ret
