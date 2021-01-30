"""

None
"""


class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        indices = {}
        for i, n in enumerate(B):
            if n not in indices:
                indices[n] = []
            indices[n].append(i)
        ans = []
        for n in A:
            ans.append(indices[n].pop())
        return ans