"""

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def try_break(s, dd, mem):
            if len(s) == 0:
                return ['']
            elif s in mem:
                return mem[s]
            ret = []
            for i in range(1, len(s) + 1):
                prev, after = s[:i], s[i:]
                if not dd.get(prev, False):
                    continue
                if len(after) == 0:
                    ret.append(prev)
                    continue
                ls = try_break(after, dd, mem)
                for bp in ls:
                    ret.append('{} {}'.format(prev, bp))
            mem[s] = ret
            return ret
        
        track = dict((word, True) for word in wordDict)
        mem = {}
        return try_break(s, track, mem)