"""
We are given two arrays words1 and words2 of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from words1 is universal if for every b in words2, b is a subset of a. 

Return a list of all universal words in words1.  You can return the words in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
 

Note:

1 <= words1.length, words2.length <= 10000
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase letters.
All words in words1[i] are unique: there isn't i != j with words1[i] == words1[j].
"""


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        tr = {}
        for w in B:
            tt = {}
            for c in w:
                if c not in tt:
                    tt[c] = 0
                tt[c] += 1
            for c, c1 in tt.iteritems():
                if c not in tr:
                    tr[c] = tt[c]
                else:
                    tr[c] = max(tr[c], tt[c])
        ret = []
        for w in A:
            tt = {}
            for c in w:
                if c not in tt:
                    tt[c] = 0
                tt[c] += 1
            for c, c1 in tr.iteritems():
                if c1 > tt.get(c, 0):
                    break
            else:
                ret.append(w)
        return ret
