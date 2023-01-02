"""

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 
Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

 
Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.


"""


class Solution:
    def calculate(self, s: str) -> int:
    	
    	### num is the current number we are constructing
    	
    	### sign is the '+' or '-' before the current number we are constructing/holding
    	### Note that we initialize sign with 1 to represent '+'
    	
    	### The last element in the stack will be the number we are updating during the 
    	### process, so put a 0 in it.
        num, sign, stack = 0, 1, [0]

        for c in s:

        	### Constructing the number.
            if c.isdigit():
                num = num*10 + int(c)

            ### Skip the space
            elif c==' ':
                continue

            ### When we see '+', we need to multiply the current number we are holding with the 
            ### sign before this number, and update the last element in the stack.
            ### We also need to reset num to 0 and sign to 1
            elif c == '+':
                stack[-1] += num * sign
                sign = 1
                num = 0

            ### Doing the same thing as '+', but reset sign to -1
            elif c == '-':
                stack[-1] += num * sign
                sign = -1
                num = 0

            ### We add sign to stack which represent the sign of this ()
            ### We also add a 0 so we can keep update while evaluating the expression inside this ()
            ### Reset num and sign again
            elif c == '(':
                stack.extend([sign,0])
                sign = 1
                num = 0

            ### pop the last element and combine it with the current num and sign we are holding (the last element inside this '()' ).
			### pop the last element again which is the sign for this '()' and muitiply them together.
			### add everything we get inside this '()' to the last element in the stack.
            elif c == ')':
                lastNum = (stack.pop() + num*sign) * stack.pop()
                stack[-1] += lastNum
                sign = 1
                num = 0
                
        ### stack should only contain one element representing everything except the last number if the expression ended with a number, so add the current num we are holding to the result.
        return stack[-1]+num*sign