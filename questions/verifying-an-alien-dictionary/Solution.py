"""

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
 
Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

 
Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.


"""


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def is_in_order(prev, word, track):
            for c1, c2 in zip(prev, word):
                if c1 == c2:
                    continue
                return track[c1] < track[c2]
            return len(prev) <= len(word)
        
        track = dict((c, i) for i, c in enumerate(order))
        prev = None
        for word in words:
            if prev is None:
                prev = word
                continue
            tmp = is_in_order(prev, word, track)
            if not tmp:
                return False
            prev = word
        return True