"""

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
 
Example 1:


Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1

 
Constraints:

1 <= n <= 19


"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={}
        def help(n):
            if n in d:
                return d[n]
            if n<=2:
                d[n]=n
                return n
            result=0
            for i in range(1,n-1):
                result+=help(i)*help(n-i-1)
            result+=2*help(n-1)
            d[n]=result
            return result
        help(n)
        return d[n]