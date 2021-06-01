"""

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.
 
Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

 
Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

 
Follow up: Could you solve it using only O(s2.length) additional memory space?

"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def is_inter(s1, s2, s3, i, j, prev, tr):
            key = (i, j, prev)
            if key in tr:
                return tr[key]
            if i == len(s1) and j == len(s2):
                return True
            elif i > len(s1) and j > len(s2):
                return False
            ret = False
            if prev <= 1:
                ii = i
                while ii < len(s1):
                    if not s1[ii] == s3[ii + j]:
                        break
                    if is_inter(s1, s2, s3, ii + 1, j, 2, tr):
                        ret = True
                        break
                    ii += 1
            if prev == 0 or prev == 2:
                jj = j
                while jj < len(s2):
                    if not s2[jj] == s3[i + jj]:
                        break
                    if is_inter(s1, s2, s3, i, jj + 1, 1, tr):
                        ret = True
                        break
                    jj += 1
            tr[key] = ret
            return ret
                    
                
        
        if not s1 and not s2 and not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        tr = {}
        return is_inter(s1, s2, s3, 0, 0, 0, tr)