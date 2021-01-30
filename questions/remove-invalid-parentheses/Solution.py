"""

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]

"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def extra_parentheses(s):
            cnt = 0
            closing, opening = 0, 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    cnt = 0
                    closing += 1
            cnt = 0
            for c in reversed(s):
                if c == ')':
                    cnt += 1
                elif c == '(':
                    cnt -= 1
                if cnt < 0:
                    cnt = 0
                    opening += 1
            return opening, closing
        
        def generate_valid(curr, index, opening, closing, ret):
            if opening == 0 and closing == 0:
                co, cc = extra_parentheses(curr)
                if co == 0 and cc == 0:
                    ret.add(''.join(curr))
                return
            if index >= len(curr):
                return
            ch = curr[index]
            if ch == '(' and opening > 0:
                curr[index] = ''
                generate_valid(curr, index + 1, opening - 1, closing, ret)
                curr[index] = '('
            elif ch == ')' and closing > 0:
                curr[index] = ''
                generate_valid(curr, index + 1, opening, closing - 1, ret)
                curr[index] = ')'
            generate_valid(curr, index + 1, opening, closing, ret)
        
        curr = list(s)
        opening, closing = extra_parentheses(curr)
        ret = set()
        generate_valid(curr, 0, opening, closing, ret)
        return list(ret)