"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st, en = 0, len(s) - 1
        while st < en:
            if s[st] != s[en]:
                s1 = st + 1
                e1 = en
                while s1 < e1:
                    if s[s1] != s[e1]:
                        break
                    s1 += 1
                    e1 -= 1
                else:
                    return True
                s1 = st
                e1 = en - 1
                while s1 < e1:
                    if s[s1] != s[e1]:
                        break
                    s1 += 1
                    e1 -= 1
                else:
                    return True
                return False
            st += 1
            en -= 1
        return True

