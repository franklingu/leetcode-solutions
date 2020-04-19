"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        track1 = {}
        track2 = {}
        for c1, c2 in zip(s, t):
            if c1 not in track1 and c2 not in track2:
                track1[c1] = c2
                track2[c2] = c1
            elif c1 not in track1 or c2 not in track2:
                return False
            else:
                if c2 != track1[c1] or c1 != track2[c2]:
                    return False
        return True
