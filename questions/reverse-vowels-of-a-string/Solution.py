"""

Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:

Input: "hello"
Output: "holle"


Example 2:

Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
 

"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        r = list(s)
        s, e = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        while s < e:
            while s < e and r[s] not in vowels:
                s += 1
            while s < e and r[e] not in vowels:
                e -= 1
            if s < e:
                r[s], r[e] = r[e], r[s]
                s += 1
                e -= 1
        return ''.join(r)