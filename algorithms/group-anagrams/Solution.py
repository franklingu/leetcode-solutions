"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        track = {}
        for ss in strs:
            cnts = collections.Counter(ss)
            cnts = tuple(sorted(cnts.items()))
            if cnts not in track:
                track[cnts] = []
            track[cnts].append(ss)
        return [v for k, v in track.items()]
