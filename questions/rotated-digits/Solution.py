"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def rotate_single(d):
            if d in set([0, 1, 8]):
                return d
            elif d == 2:
                return 5
            elif d == 5:
                return 2
            elif d == 6:
                return 9
            elif d == 9:
                return 6
            else:
                return -1

        def rotate_number(n):
            r = []
            for c in str(n):
                cr = rotate_single(int(c))
                if cr < 0:
                    return -1
                r.append(str(cr))
            return int(''.join(r))

        r = 0
        for n in xrange(1, N + 1):
            nr = rotate_number(n)
            if nr > 0 and nr != n:
                r += 1
        return r

