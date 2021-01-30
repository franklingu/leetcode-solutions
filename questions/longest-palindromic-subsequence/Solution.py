"""

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example 1:
Input:

"bbbab"

Output:


4

One possible longest palindromic subsequence is "bbbb".

 
Example 2:
Input:

"cbbd"

Output:


2

One possible longest palindromic subsequence is "bb".
 
Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.


"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][(j - 1)] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][(j - 1)])
        return dp[0][(n-1)]