"""

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"


Note:
In the string, each word is separated by single space and there will not be any extra space in the string.

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse_pos(s, st, ed):
            while st < ed:
                s[ed], s[st] = s[st], s[ed]
                st += 1
                ed -= 1

        def reverse_in_words(s):
            start_idx = 0
            for i, c in enumerate(s):
                if c == ' ' and i != start_idx:
                    reverse_pos(s, start_idx, i - 1)
                    start_idx = i + 1
                elif c == ' ' and i == start_idx:
                    start_idx = i + 1
                else:
                    pass
            if start_idx < len(s):
                reverse_pos(s, start_idx, len(s) - 1)
            return s

        if not s:
            return s
        return ''.join(reverse_in_words(list(s)))