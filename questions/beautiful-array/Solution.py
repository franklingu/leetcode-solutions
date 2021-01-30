"""

For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
Given N, return any beautiful array A.  (It is guaranteed that one exists.)
 
Example 1:

Input: 4
Output: [2,1,4,3]


Example 2:

Input: 5
Output: [3,1,2,5,4]
 

Note:

1 <= N <= 1000


 

"""


class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        ### method 1: observation from output
#         def helper(nums):
#             if len(nums) == 1:
#                 return nums
#             even = [e for i, e in enumerate(nums) if i % 2 == 0]
#             odd = [e for i, e in enumerate(nums) if i % 2 == 1]
#             return helper(even) + helper(odd)
        
#         nums = list(range(1, N + 1))
#         return helper(nums)
        ### method 2: beautiful algo making use of nature of beautiful array when building up
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= N]
