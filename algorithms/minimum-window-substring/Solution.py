"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ### method 1, the complexity does not meet requirement, but AC
        # counter = Counter(t)
        # track = dict((k, []) for k in counter)
        # num = len(t)
        # indices = []
        # mlen = None
        # start = None
        # for i, c in enumerate(s):
        #     if c not in counter:
        #         continue
        #     if len(track[c]) == counter[c]:
        #         track[c].pop(0)
        #         track[c].append(i)
        #     else:
        #         track[c].append(i)
        #         num -= 1
        #     if num == 0:
        #         midx = None
        #         for ls in track.values():
        #             if midx is None or midx > ls[0]:
        #                 midx = ls[0]
        #         if mlen is None or mlen > (i - midx + 1):
        #             mlen = i - midx + 1
        #             start = midx
        # return s[start:start + mlen] if mlen else ''
        ### method 2, using idea of two pointer
        if not s or not t:
            return ''
        need, missing = Counter(t), len(t)
        mlen, start, mstart = None, 0, 0
        for i, c in enumerate(s):
            if c not in need:
                continue
            need[c] -= 1
            if need[c] >= 0:
                missing -= 1
            if missing > 0:
                continue
            while start <= i and (s[start] not in need or need[s[start]] < 0):
                if s[start] in need:
                    need[s[start]] += 1
                start += 1
            clen = i - start + 1
            if mlen is None or mlen > clen:
                mlen = clen
                mstart = start
        if mlen is None:
            return ''
        return s[mstart:mstart + mlen]
