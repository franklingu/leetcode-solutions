"""

None
"""


from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        similar_map = defaultdict(set)
        for w1, w2 in pairs:
            similar_map[w1].add(w2)
            similar_map[w2].add(w1)
        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue
            if w1 in similar_map.get(w2, []):
                continue
            return False
        return True
            