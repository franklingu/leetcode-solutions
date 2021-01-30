"""

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

"""


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def calc(num1, num2, op):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            
        def preprocess(s):
            stack = []
            for c in s:
                if c in set('+-*'):
                    stack.append(c)
                else:
                    if not stack or stack[-1] in set('+-*'):
                        stack.append(ord(c) - ord('0'))
                        if len(stack) == 2 and stack[0] == '-':
                            stack[0] = -stack[1]
                            stack.pop()
                    else:
                        curr = ord(c) - ord('0')
                        if stack[-1] < 0:
                            curr = -curr
                        stack[-1] = stack[-1] * 10 + curr
            return stack
            
        def generate_result(ops, start, end, exp):
            if start > end:
                return []
            elif start == end:
                pos = ops[start]
                return [calc(exp[pos - 1], exp[pos + 1], exp[pos])]
            ret = []
            for i in range(start, end + 1):
                if i == start:
                    left = set([exp[ops[i] - 1]])
                    right = generate_result(ops, i + 1, end, exp)
                elif i == end:
                    left = generate_result(ops, start, i - 1, exp)
                    right = set([exp[ops[i] + 1]])
                else:
                    left = generate_result(ops, start, i - 1, exp)
                    right = generate_result(ops, i + 1, end, exp)
                for e1 in left:
                    for e2 in right:
                        ret.append(calc(e1, e2, exp[ops[i]]))
            return ret
        
        exp = preprocess(input)
        ops = [i for i, c in enumerate(exp) if c in set('+-*')]
        if not ops:
            return exp
        ret = generate_result(ops, 0, len(ops) - 1, exp)
        return ret