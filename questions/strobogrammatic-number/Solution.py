"""

None
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        track = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }
        start, end = 0, len(num) - 1
        while start <= end:
            if start == end:
                if num[start] not in '018':
                    return False
                else:
                    return True
            sc = ord(num[start]) - ord('0')
            ec = ord(num[end]) - ord('0')
            if track.get(sc, -1) != ec:
                return False
            start += 1
            end -= 1
        return True