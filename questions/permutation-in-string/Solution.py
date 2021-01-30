"""

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
 
Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

 
Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


"""


class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        from collections import Counter
        counter = Counter(p)
        start = 0
        c2 = {}
        for i, c in enumerate(s):
            if c not in counter:
                start = i + 1
                c2 = {}
                continue
            if c not in c2:
                c2[c] = 1
            else:
                c2[c] += 1
            if i - start + 1 < len(p):
                continue
            elif i - start + 1 > len(p):
                c2[s[start]] -= 1
                start += 1
            if c2 == counter:
                return True
        return False
        