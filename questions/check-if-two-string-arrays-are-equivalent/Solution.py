"""

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
 
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

 
Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.


"""


class Solution:
    def arrayStringsAreEqual(self, w1: List[str], w2: List[str]) -> bool:
        i1, i2, c1, c2 = 0, 0, 0, 0
        while True:
            if i1 >= len(w1) and i2 >= len(w2):
                return True
            elif i1 >= len(w1) or i2 >= len(w2):
                return False
            e1 = w1[i1][c1]
            e2 = w2[i2][c2]
            if e1 != e2:
                return False
            c1 += 1
            if c1 >= len(w1[i1]):
                c1 = 0
                i1 += 1
            c2 += 1
            if c2 >= len(w2[i2]):
                c2 = 0
                i2 += 1
        return True