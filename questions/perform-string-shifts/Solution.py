"""

None
"""


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        distance = 0
        for d, step in shift:
            if d == 0:
                distance += step
            else:
                distance -= step
        distance = distance % len(s)
        return s[distance:] + s[:distance]