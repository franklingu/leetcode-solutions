"""

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


"""


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        t, c, p = [], 0, None
        for n in reversed(nums):
            if p is None:
                c += 1
            else:
                if n == p:
                    c += 1
                else:
                    t.append((p, c))
                    c = 1
            p = n
        if p is not None:
            t.append((p, c))
        r = 0
        p, s = None, 0
        for n, c in t:
            if p is None:
                s = c
                p = n
                continue
            r += (p - n) * s
            p = n
            s += c
        return r