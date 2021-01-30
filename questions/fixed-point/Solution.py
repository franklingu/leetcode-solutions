"""

None
"""


class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, a in enumerate(A):
            if i == a:
                return i
        return -1