"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        nums = [[]]
        ops = []
        for c in s:
            if c == ' ':
                continue
            if c in set('+-*/') and nums[0]:
                ops.append(c)
                nums[-1] = int(''.join(nums[-1]))
                nums.append([])
            else:
                nums[-1].append(c)
        nums[-1] = int(''.join(nums[-1]))
        nums2 = []
        ops2 = []
        for i in range(len(nums)):
            if i == 0:
                nums2.append(nums[i])
                continue
            op = ops[i - 1]
            if op == '+' or op == '-':
                ops2.append(op)
                nums2.append(nums[i])
                continue
            elif op == '*':
                nums2[-1] = nums2[-1] * nums[i]
            else:
                nums2[-1] = nums2[-1] // nums[i]
        nums = nums2
        ops = ops2
        res = None
        for i in range(len(nums)):
            if i == 0:
                res = nums[i]
                continue
            op = ops[i - 1]
            if op == '+':
                res = res + nums[i]
            else:
                res = res - nums[i]
        return res
