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


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def get_extra(s):
            closing = 0
            stk = []
            for i, c in enumerate(s):
                if c == '(':
                    stk.append(i)
                elif c == ')':
                    if not stk:
                        closing += 1
                    else:
                        stk.pop()
            return len(stk), closing
            
        def generate_valid(s, i, op, cc, opening, closing, ret):
            if i >= len(s):
                if opening != 0 or closing != 0:
                    return
                op, cc = get_extra(s)
                if op == 0 and cc == 0:
                    ret.add(''.join(s))
                return
            c = s[i]
            if c != '(' and c != ')':
                generate_valid(s, i + 1, op, cc, opening, closing, ret)
                return
            elif c == '(':
                if opening > 0:
                    s[i] = ''
                    generate_valid(s, i + 1, op, cc, opening - 1, closing, ret)
                    s[i] = c
                generate_valid(s, i + 1, op + 1, cc, opening, closing, ret)
            elif c == ')':
                if closing > 0:
                    s[i] = ''
                    generate_valid(s, i + 1, op, cc, opening, closing - 1, ret)
                    s[i] = c
                if op > cc:
                    generate_valid(s, i + 1, op, cc + 1, opening, closing, ret)
            
        
        opening, closing = get_extra(s)
        ret = set()
        generate_valid(list(s), 0, 0, 0, opening, closing, ret)
        return list(ret)