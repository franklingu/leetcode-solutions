"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(num):
            if 0 < num < 10:
                return True
            for ch in set(str(num)):
                digit = int(ch)
                if digit != 0 and num % digit == 0:
                    continue
                else:
                    return False
            return True

        ret = []
        for num in xrange(left, right + 1):
            if isSelfDividing(num):
                ret.append(num)
        return ret

