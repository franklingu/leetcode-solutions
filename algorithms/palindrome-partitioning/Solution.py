"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def isPal(s):
            return s == s[::-1]
        
        def backtrack(s, l):
            if not s:
                ret.append(l)
                return
            for i in range(1, len(s)+1):
                if isPal(s[:i]):
                    backtrack(s[i:], l+[s[:i]])
        
        backtrack(s, [])
        return ret
