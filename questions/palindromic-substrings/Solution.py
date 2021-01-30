"""

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

 
Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 
Note:

The input string length won't exceed 1000.

 
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindrome(start, end, s):
            if end >= len(s):
                return 0
            count = 0
            st, en = start, end
            while st >= 0 and en < len(s) and s[st] == s[en]:
                count += 1
                st -= 1
                en += 1
            return count
        
        ret = 0
        for i in range(len(s)):
            ret += count_palindrome(i, i, s)
            ret += count_palindrome(i, i + 1, s)
        return ret