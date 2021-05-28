"""

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.
Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.

 
Constraints:

0 <= words.length <= 10^3
0 <= words[i].length <= 10^3
words[i] consists only of lowercase English letters.


"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ss = 0
        words.sort(key=lambda x: -len(x))
        for i in range(len(words)):
            w1 = set(words[i])
            for j in range(i + 1, len(words)):
                for c in words[j]:
                    if c in w1:
                        break
                else:
                    ss = max(ss, len(words[i]) * len(words[j]))
        return ss


class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        cache = dict()
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << ord(c)
            cache[mask]= max(cache.get(mask,0), len(word)) 
        max_pr = 0
        for i in cache:
            for j in cache:
                if not i & j:
                    max_pr = max(max_pr , cache[i]*cache[j])
        return max_pr
