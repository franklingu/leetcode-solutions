"""

None
"""


class Solution:
    def countElements(self, arr: List[int]) -> int:
        res = 0
        ss = set(arr)
        for a in arr:
            if a + 1 in ss:
                res += 1
        return res