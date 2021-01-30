"""

None
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) < len(t):
            s, t = t, s
        i, j = 0, 0
        seen_change = False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if seen_change:
                    return False
                seen_change = True
                if len(s) > len(t):
                    i += 1
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
        if i != len(s) or j != len(t):
            if not seen_change:
                seen_change = True
            else:
                return False
        return seen_change