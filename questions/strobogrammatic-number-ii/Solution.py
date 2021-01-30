"""

None
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def build_numbers(start, end, left, right, track, ret):
            if start > end:
                if len(left) + len(right) > 1 and left[0] == 0:
                    return
                ret.append(left + right[::-1])
                return
            elif start == end:
                for n1, n2 in track:
                    if n1 != n2:
                        continue
                    left.append(n1)
                    build_numbers(start + 1, end - 1, left, right, track, ret)
                    left.pop()
                return
            for n1, n2 in track:
                left.append(n1)
                right.append(n2)
                build_numbers(start + 1, end - 1, left, right, track, ret)
                left.pop()
                right.pop()
        
        track = [(0, 0), (1, 1), (6, 9), (8, 8), (9, 6)]
        left, right = [], []
        ret = []
        build_numbers(0, n - 1, left, right, track, ret)
        return [''.join((str(e) for e in n)) for n in ret]