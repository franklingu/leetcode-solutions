"""

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
 
Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false

 
Constraints:

0 <= s.length <= 20
0 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match_pattern(s, p, sidx, pidx, track):
            if (sidx, pidx) in track:
                return track[(sidx, pidx)]
            if sidx >= len(s) and pidx >= len(p):
                return True
            elif sidx >= len(s):
                if (len(p) - pidx) % 2 != 0:
                    track[(sidx, pidx)] = False
                    return False
                for i in range(pidx, len(p)):
                    if (i - pidx) % 2 == 1:
                        if p[i] != '*':
                            track[(sidx, pidx)] = False
                            return False
                track[(sidx, pidx)] = True
                return True
            elif pidx >= len(p):
                return False
            if pidx == len(p) - 1:
                if sidx != len(s) - 1:
                    track[(sidx, pidx)] = False
                    return False
                if p[pidx] == '.' or p[pidx] == s[sidx]:
                    track[(sidx, pidx)] = True
                    return True
                track[(sidx, pidx)] = False
                return False
            curr, nn = p[pidx], p[pidx + 1]
            if nn != '*':
                if curr != s[sidx] and curr != '.':
                    track[(sidx, pidx)] = False
                    return False
                ret = match_pattern(s, p, sidx + 1, pidx + 1, track)
                track[(sidx, pidx)] = ret
                return ret
            for i in range(len(s) - sidx + 1):
                if i > 0 and (s[sidx + i - 1] != curr and curr != '.'):
                    break
                tmp = match_pattern(s, p, sidx + i, pidx + 2, track)
                if tmp:
                    track[(sidx, pidx)] = True
                    return True
            track[(sidx, pidx)] = False
            return False
        
        track = {}
        return match_pattern(s, p, 0, 0, track)