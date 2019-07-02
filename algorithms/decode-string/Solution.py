'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

'''
A natural recursion/stack based problem
'''


class Solution:
    def decodeString(self, s: str) -> str:
        if '[' not in s:
            return s
        num = 0
        ret = []
        start, cnt = -1, 0
        for i, c in enumerate(s):
            if c == '[':
                cnt += 1
                if start < 0:
                    start = i
            elif c == ']':
                cnt -= 1
                if cnt == 0:
                    ret.append(self.decodeString(s[start + 1:i]) * num)
                    num = 0
                    start = -1
            elif cnt == 0 and ord('0') <= ord(c) <= ord('9'):
                num = num * 10 + ord(c) - ord('0')
            elif cnt == 0:
                ret.append(c)
        return ''.join(ret)
