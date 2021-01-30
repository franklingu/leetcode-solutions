"""

Given an integer, return its base 7 string representation.
Example 1:

Input: 100
Output: "202"


Example 2:

Input: -7
Output: "-10"


Note:
The input will be in range of [-1e7, 1e7].

"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            is_negative = True
            num = -num
        else:
            is_negative = False
        r = []
        while num >= 7:
            num, d = divmod(num, 7)
            r.append(str(d))
        if num > 0:
            r.append(str(num))
        can = ''.join(reversed(r))
        return can if not is_negative else '-' + can