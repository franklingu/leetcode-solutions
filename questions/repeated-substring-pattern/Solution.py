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

# easy and quick solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def canDivide(s, i):
            return s[:i] * (len(s) // i) == s
        
        for i in range(len(s)):
            if i == 0:
                continue
            if len(s) % i == 0:
                if canDivide(s, i):
                    return True
        return False

class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def build_prefix(s):
            prefix = [0 for _ in s]
            runner, target = 1, 0
            while runner < len(s):
                if s[runner] == s[target]:
                    target += 1
                    prefix[runner] = target
                    runner += 1
                else:
                    if target == 0:
                        runner += 1
                    else:
                        target = prefix[target - 1]
            return prefix
        
        prefix = build_prefix(s)
        if prefix[len(s) - 1] == 0:
            return False
        return len(s) % (len(s) - prefix[len(s) - 1]) == 0
