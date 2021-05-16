"""

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
	
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.



An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
Given a string s, return true if s is a valid number.
 
Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false

Example 4:

Input: s = ".1"
Output: true

 
Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.


"""


class Solution:
    def isNumber(self, s: str) -> bool:
        def isPureDigit(s):
            if not s:
                return False
            return s.isnumeric()
        
        def isInt(s):
            if not s:
                return False
            idx = 0
            if s[0] == '+' or s[0] == '-':
                idx = 1
            return isPureDigit(s[idx:])
        
        def isDecimal(s):
            if len(s) <= 1:
                return False
            idx = s.find('.')
            if idx == -1:
                return False
            start = 0
            if s[0] == '+' or s[0] == '-':
                start = 1
            first, second = s[start:idx], s[idx + 1:]
            if idx == 0:
                return isPureDigit(second)
            elif idx == len(s) - 1:
                return isPureDigit(first)
            else:
                return (not first or isPureDigit(first)) and isPureDigit(second)
        
        idx = -1
        if 'e' in s:
            idx = s.find('e')
        elif 'E' in s:
            idx = s.find('E')
        if idx == -1:
            return isInt(s) or isDecimal(s)
        return (isInt(s[:idx]) or isDecimal(s[:idx])) and isInt(s[idx + 1:])