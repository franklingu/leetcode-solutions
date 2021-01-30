"""

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
 
Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def find_divisors(l):
            divs = []
            for d in xrange(1, l):
                if l % d == 0:
                    divs.append(d)
            return divs

        def can_repeat(s, d, l):
            r = s[:d]
            t = d
            while t < l:
                if r == s[t:t + d]:
                    pass
                else:
                    return False
                t += d
            return True

        l = len(s)
        divs = find_divisors(l)
        for div in divs:
            if can_repeat(s, div, l):
                return True
        return False