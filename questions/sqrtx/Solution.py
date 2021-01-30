"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        elif x < 2:
            return x
        ret = x / 2
        cal = ret * ret
        while True:
            if cal == x:
                break
            prev = ret
            ret = (ret + x / ret) / 2
            next_cal = ret * ret
            if (cal > x and next_cal < x):
                break
            elif (cal < x and next_cal > x):
                ret = prev
                break
            elif prev == ret:
                break
        return ret
