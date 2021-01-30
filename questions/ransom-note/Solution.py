"""

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

 
Constraints:

You may assume that both strings contain only lowercase letters.


"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1, c2 = {}, {}
        for c in ransomNote:
            if c not in c1:
                c1[c] = 0
            c1[c] += 1
        for c in magazine:
            if c not in c2:
                c2[c] = 0
            c2[c] += 1
        for c, n in c1.items():
            if c not in c2:
                return False
            if c2[c] < n:
                return False
        return True
        