"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:
Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.


 Note:

 1 <= paragraph.length <= 1000.
 1 <= banned.length <= 100.
 1 <= banned[i].length <= 10.
 The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
 paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
 Different words in paragraph are always separated by a space.
 There are no hyphens or hyphenated words.
 Words only consist of letters, never apostrophes or other punctuation symbols.
"""
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = paragraph.lower()
        b = set(banned)
        w, ws = [], []
        for c in p:
            if c.isalpha():
                w.append(c)
            elif c == ' ':
                ws.append(''.join(w))
                w = []
            else:
                pass
        if w:
            ws.append(''.join(w))
        track = {}
        for w in ws:
            if w in b:
                continue
            if w not in track:
                track[w] = 0
            track[w] += 1
        m, r = 0, None
        for w, c in track.iteritems():
            if c > m:
                m = c
                r = w
        return r
