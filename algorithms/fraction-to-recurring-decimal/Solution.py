"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = False
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            is_negative = True
        sign = '-' if is_negative else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part, float_part = divmod(numerator, denominator)
        if float_part == 0:
            return '{}{}'.format(sign, str(int_part))
        track = {}
        float_repr = []
        while float_part > 0:
            q, float_part = divmod(float_part * 10, denominator)
            if (q, float_part) in track:
                prev_index = track[(q, float_part)]
                float_repr.insert(prev_index, '(')
                float_repr.append(')')
                break
            else:
                track[(q, float_part)] = len(float_repr)
                float_repr.append(q)
        return '{}{}.{}'.format(sign, str(int_part), ''.join(( str(elem) for elem in float_repr )))
        