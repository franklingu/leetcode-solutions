"""

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.
Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.
You may return the answer in any order.
 
Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Example 3:

Input: n = 2, k = 0
Output: [11,22,33,44,55,66,77,88,99]

Example 4:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Example 5:

Input: n = 2, k = 2
Output: [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]

 
Constraints:

2 <= n <= 9
0 <= k <= 9


"""


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return list(xrange(10))
        track = dict()
        for el in xrange(10):
            e1, e2 = el + K, el - K
            if 0 <= e1 <= 9:
                track[el] = [e1]
            if 0 <= e2 <= 9:
                if el not in track:
                    track[el] = []
                track[el].append(e2)
        ret = []
        for idx in xrange(N):
            if idx == 0:
                for el in track.keys():
                    if el == 0:
                        continue
                    ret.append([el])
                continue
            addon = []
            for candidate in ret:
                end = candidate[-1]
                for el in track[end]:
                    tmp = list(candidate)
                    tmp.append(el)
                    addon.append(tmp)
            ret = addon
        ret = [int(''.join([str(el) for el in ls])) for ls in ret]
        ss = set()
        res = []
        for n in ret:
            if n not in ss:
                ss.add(n)
                res.append(n)
            else:
                continue
        return res