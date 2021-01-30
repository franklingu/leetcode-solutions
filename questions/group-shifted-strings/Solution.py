"""

None
"""


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        track = {}
        for s in strings:
            diffs = []
            for i, c in enumerate(s):
                if i == 0:
                    continue
                diffs.append((ord(c) - ord(s[i - 1]) + 26) % 26)
            key = tuple(diffs)
            if key not in track:
                track[key] = []
            track[key].append(s)
        return list(track.values())