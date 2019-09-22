"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, interval in enumerate(intervals):
            if interval[0] >= newInterval[0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
        ret = []
        for interval in intervals:
            if not ret or ret[-1][1] < interval[0]:
                ret.append(interval)
            else:
                ret[-1] = [ret[-1][0], max(ret[-1][1], interval[1])]
        return ret
