"""

Given a list of words, each word consists of English lowercase letters.
Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".
A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
Return the longest possible length of a word chain with words chosen from the given list of words.
 
Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5

 
Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.


"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def fill_pre(w2, ss, dd):
            if w2 not in ss:
                return 0
            if w2 in dd:
                return dd[w2]
            m = 1
            for i in range(len(w2)):
                w = w2[:i] + w2[i + 1:]
                if w not in ss:
                    continue
                m = max(m, fill_pre(w, ss, dd) + 1)
            dd[w2] = m
            return dd[w2]
        
        words.sort(key=lambda x: len(x))
        dd = {}
        ss = set(words)
        for w in reversed(words):
            fill_pre(w, ss, dd)
        return max(dd.values())
                