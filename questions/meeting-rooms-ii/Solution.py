"""

None
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        from collections import Counter
        start = Counter([interval[0] for interval in intervals])
        end = Counter([interval[1] for interval in intervals])
        nums = set(start.keys()).union(set(end.keys()))
        mm = 0
        curr = 0
        for n in sorted(nums):
            if n in end:
                curr -= end[n]
            if n in start:
                curr += start[n]
            mm = max(mm, curr)
        return mm