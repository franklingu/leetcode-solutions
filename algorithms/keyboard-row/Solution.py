"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

![American keyboard](https://leetcode.com/static/images/problemset/keyboard.png)

Example 1:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]

Note:

    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.

"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        mapping = [
            set('zxcvbnm'),
            set('asdfghjkl'),
            set('qwertyuiop')
        ]
        ret = []
        for s in words:
            prev_idx = None
            is_okay = True
            for c in s:
                for idx, row in enumerate(mapping):
                    if c in row:
                        curr_idx = idx
                        if prev_idx is None:
                            prev_idx = curr_idx
                        if prev_idx != curr_idx:
                            is_okay = False
                            break
            if is_okay:
                ret.append(s)
        return ret
