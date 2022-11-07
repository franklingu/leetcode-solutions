"""

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.


"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def build_prefix(needle):
            prefix = [0 for _ in needle]
            runner, target = 1, 0
            while runner < len(needle):
                if needle[runner] == needle[target]:
                    target += 1
                    prefix[runner] = target
                    runner += 1
                else:
                    if target == 0:
                        runner += 1
                    else:
                        target = prefix[target - 1]
            return prefix
        
        def find_match(haystack, needle, prefix):
            i, j = 0, 0
            while i < len(haystack):
                if haystack[i] == needle[j]:
                    j += 1
                    if len(needle) == j:
                        return i - len(needle) + 1
                    i += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = prefix[j - 1]
            return -1
            
        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0
        prefix = build_prefix(needle)
        return find_match(haystack, needle, prefix)