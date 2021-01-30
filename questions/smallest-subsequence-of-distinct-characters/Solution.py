"""
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

"""

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        visited = set()
        
        for i, symbol in enumerate(s):
            if symbol in visited:
                continue
            while (symbol < stack[-1] and last_occ[stack[-1]] > i):
                visited.remove(stack.pop())
            stack.append(symbol)
            visited.add(symbol)  
        return "".join(stack)[1:]
