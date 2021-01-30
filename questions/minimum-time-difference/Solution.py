"""

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 
Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

 
Constraints:

2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".


"""


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def to_minutes(ts):
            return int(ts[:2]) * 60 + int(ts[3:])
        
        minutes = [to_minutes(el) for el in timePoints]
        minutes.sort()
        prev, mm = None, abs(minutes[0] + 60 * 24 - minutes[-1])
        for num in minutes:
            if prev is None:
                prev = num
                continue
            if mm > num - prev:
                mm = num - prev
            prev = num
        return mm