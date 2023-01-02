"""

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
 
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.


"""


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        tr = Counter(words[0])
        for word in words:
            counter = Counter(word)
            new_tr = {}
            for c in tr:
                if c not in counter:
                    continue
                new_tr[c] = min(tr[c], counter[c])
            tr = new_tr
        ret = []
        for c, l in tr.items():
            if l <= 0:
                continue
            for _ in range(l):
                ret.append(c)
        return ret