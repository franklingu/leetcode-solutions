"""

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
 
Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1

Example 3:

Input: s = "bb"
Output: 2

 
Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.


"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        tr = {}
        for c in s:
            if c not in tr:
                tr[c] = 0
            tr[c] += 1
        odd_max = -1
        r = 0
        for c, n in tr.items():
            if n % 2 == 0:
                r += n
            else:
                r += (n - 1)
                odd_max = max(odd_max, n)
        if odd_max > 0:
            r += 1
        return r