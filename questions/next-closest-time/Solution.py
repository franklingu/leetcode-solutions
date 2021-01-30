"""

None
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def generate_times(digits, curr):
            if len(curr) == 4:
                first, second = curr[0] + curr[1], curr[2] + curr[3]
                if 0 <= int(first) < 24 and 0 <= int(second) < 60:
                    yield first + ':' + second
                return
            for digit in digits:
                curr.append(digit)
                yield from generate_times(digits, curr)
                curr.pop()
        
        def calculate_diff(time, nt):
            first1, second1 = time.split(':')
            first2, second2 = nt.split(':')
            time = int(first1) * 60 + int(second1)
            nt = int(first2) * 60 + int(second2)
            if nt <= time:
                nt += 24 * 60
            return nt - time
        
        digits = set([c for c in time if c.isnumeric()])
        min_diff, ret = None, None
        for nt in generate_times(digits, []):
            diff = calculate_diff(time, nt)
            if min_diff is None or diff < min_diff:
                min_diff = diff
                ret = nt
        return ret