"""

Given a string s, return the longest palindromic substring in s.
 
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"

 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # get the longest palindrome, l, r are the middle indexes   
        # from inner to outer
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]
        
        ### method 1, based on dp
        # if not s:
        #     return ''
        # track = [[0] * len(s) for _ in range(len(s))]
        # mm, ty, tx = 1, 0, 0
        # for x in range(len(s)):
        #     i, j = 0, x
        #     while j < len(s):
        #         if s[i] == s[j] and x == 0:
        #             track[i][j] = 1
        #         elif s[i] == s[j] and x == 1:
        #             track[i][j] = 2
        #             mm = 2
        #             ty, tx = i, j
        #         elif s[i] == s[j] and track[i + 1][j - 1] != 0:
        #             track[i][j] = track[i + 1][j - 1] + 2
        #             if track[i][j] > mm:
        #                 mm = track[i][j]
        #                 ty, tx = i, j
        #         i += 1
        #         j += 1
        # return s[ty:tx + 1]
    
        ### method 2, just starting from middle
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
                    
        