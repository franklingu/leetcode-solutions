"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        dp = [[0] * len(text2) for _ in text1]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    dp[i][j] = 1 if i < 1 or j < 1 else dp[i - 1][j - 1] + 1
                    continue
                if i < 1:
                    n1 = 0
                else:
                    n1 = dp[i - 1][j]
                if j < 1:
                    n2 = 0
                else:
                    n2 = dp[i][j - 1]
                dp[i][j] = max(n1, n2)
        return dp[-1][-1]
