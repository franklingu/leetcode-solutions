"""


Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.  If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = []
        ts = {}
        for i, t in enumerate(reversed(T)):
            mmax = None
            for t2 in range(t + 1, 101):
                if t2 not in ts:
                    continue
                if mmax is None or ts[t2] > mmax:
                    mmax = ts[t2]
            ret.append(i - mmax if mmax is not None else 0)
            ts[t] = i
        return ret[::-1]