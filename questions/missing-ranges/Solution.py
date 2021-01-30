"""

None
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def convert_repr(ret):
            res = []
            for l, u in ret:
                if l == u:
                    res.append(str(l))
                else:
                    res.append('{}->{}'.format(l, u))
            return res
        
        ret = []
        prev = lower - 1
        for n in nums:
            if prev + 1 < n:
                ret.append([prev + 1, n - 1])
            prev = n
        if prev + 1 <= upper:
            ret.append([prev + 1, upper])
        return convert_repr(ret)