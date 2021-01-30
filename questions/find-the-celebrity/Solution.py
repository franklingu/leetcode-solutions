"""

None
"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        guess = 0
        for i in xrange(n):
            if knows(guess, i):
                guess = i
        for i in xrange(n):
            if i != guess and knows(guess, i):
                return -1
        for i in xrange(n):
            if i != guess and not knows(i, guess):
                return -1
        return guess