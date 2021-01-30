"""


Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"



Example 2:

Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"


Note:

All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.


"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubSequence(s, ss):
            i, j = 0, 0
            while i < len(s) and j < len(ss):
                while i< len(s) and ss[j] != s[i]:
                    i += 1
                if i < len(s):
                    j += 1
                    i += 1
            return j >= len(ss)
            
        ret = ''
        for ss in d:
            if isSubSequence(s, ss):
                if len(ss) > len(ret) or (len(ss) == len(ret) and ss < ret):
                    ret = ss
        return ret