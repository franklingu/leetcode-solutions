"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def transform(s):
            r = []
            for c in s:
                if c == '#' and r:
                    del r[-1]
                elif c == '#':
                    pass
                else:
                    r.append(c)
            return r

        # Simple solution
        # s = transform(S)
        # t = transform(T)
        # return s == t
        d1 = d2 = 0
        l1, l2 = len(S) - 1, len(T) - 1
        while l1 >= 0 or l2 >= 0:
            if l1 < 0:
                c1 = None
            else:
                c1 = S[l1]
            if c1 == '#':
                d1 += 1
                l1 -= 1
                c1 = None
            elif c1 != '#' and d1 > 0:
                d1 -= 1
                l1 -= 1
                c1 = None
            if l2 < 0:
                c2 = None
            else:
                c2 = T[l2]
            if c2 == '#':
                d2 += 1
                l2 -= 1
                c2 = None
            elif c2 != '#' and d2 > 0:
                d2 -= 1
                l2 -= 1
                c2 = None
            if c1 is not None and c2 is not None:
                if c1 != c2:
                    return False
                else:
                    l1 -= 1
                    l2 -= 1
            elif (l1 < 0 and c2 is not None) or (l2 < 0 and c1 is not None):
                return False
        return True
