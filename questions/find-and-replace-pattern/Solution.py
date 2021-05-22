"""

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
 
Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.

Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]

 
Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.


"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_match(word, pat):
            if len(word) != len(pat):
                return False
            tr1, tr2 = {}, {}
            for c1, c2 in zip(word, pat):
                if c1 not in tr1 and c2 not in tr2:
                    tr1[c1] = c2
                    tr2[c2] = c1
                    continue
                elif c1 in tr1 and c2 in tr2:
                    if c2 != tr1[c1] or c1 != tr2[c2]:
                        return False
                else:
                    return False
            return True
        
        ret = []
        for word in words:
            if is_match(word, pattern):
                ret.append(word)
        return ret