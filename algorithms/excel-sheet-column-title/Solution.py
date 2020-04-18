"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        def find_char(c):
            return chr(ord('A') + c - 1)

        ret = []
        while n > 0:
            n, r = divmod(n, 26)
            if r == 0:
                r = 26
                n -= 1
            ret.append(find_char(r))
        return ''.join(reversed(ret))
