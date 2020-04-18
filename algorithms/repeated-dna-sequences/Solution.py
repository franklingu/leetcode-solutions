"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        track = {}
        ret = set()
        for i in range(10, len(s) + 1):
            sub = s[i - 10:i]
            if sub not in track:
                track[sub] = True
            else:
                ret.add(sub)
        return list(ret)
