"""

You are given a 0-indexed array of unique strings words.
A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < word.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.

Return an array of all the palindrome pairs of words.
 
Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]

 
Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.


"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wmap, ans = {}, []
        for i in range(len(words)):
            wmap[words[i]] = i
        for i in range(len(words)):
            if words[i] == "":
                for j in range(len(words)):
                    w = words[j]
                    if self.isPal(w, 0, len(w)-1) and j != i:
                        ans.append([i, j])
                        ans.append([j, i])
                continue
            bw = words[i][::-1]
            if bw in wmap:
                res = wmap[bw]
                if res != i: ans.append([i, res])
            for j in range(1, len(bw)):
                if self.isPal(bw, 0, j - 1) and bw[j:] in wmap:
                    ans.append([i, wmap[bw[j:]]])
                if self.isPal(bw, j, len(bw)-1) and bw[:j] in wmap:
                    ans.append([wmap[bw[:j]], i])
        return ans

    def isPal(self, word: str, i: int, j: int) -> bool:
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True