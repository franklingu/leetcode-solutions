"""


Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.


Example 1:

Input:
26

Output:
"1a"


Example 2:

Input:
-1

Output:
"ffffffff"


"""


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        curr = []
        ret = []
        for i in xrange(32):
            curr.append(str(num & 0x01))
            num = num >> 1
            if len(curr) == 4:
                n = int(''.join(reversed(curr)), 2)
                if n < 10:
                    ret.append(str(n))
                else:
                    ret.append(chr(ord('a') + n - 10))
                curr = []
        cleaned = []
        is_ok = False
        for i, n in enumerate(reversed(ret)):
            if n != '0':
                is_ok = True
            if is_ok:
                cleaned.append(n)
        if not cleaned:
            return '0'
        return ''.join(cleaned)