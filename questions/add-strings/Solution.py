"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def to_digit(c):
            if c is None:
                return 0
            return ord(c) - ord('0')
        
        def to_char(d):
            if d > 9:
                carry = 1
                d = d % 10
            else:
                carry = 0
            return chr(ord('0') + d), carry

        from itertools import izip_longest
        carry = 0
        ret = []
        for c1, c2 in izip_longest(reversed(num1), reversed(num2)):
            d1 = to_digit(c1)
            d2 = to_digit(c2)
            d, carry = to_char(d1 + d2 + carry)
            ret.append(d)
        if carry > 0:
            ret.append(to_char(carry)[0])
        return ''.join(reversed(ret))