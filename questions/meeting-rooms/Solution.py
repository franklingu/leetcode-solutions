"""

None
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = None
        for interval in intervals:
            if prev is None:
                prev = interval
                continue
            if prev[1] > interval[0]:
                return False
            prev = interval
        return True