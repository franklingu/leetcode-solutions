"""

Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example 1:


Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].




"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nl, 0] for nl in nestedList][::-1]
        self.num = None

    def next(self):
        """
        :rtype: int
        """
        if self.num is not None:
            num = self.num
            self.num = None
            return num
        curr, nl = None, None
        while curr is None and self.stack:
            nl, idx = self.stack[-1]
            if nl.isInteger():
                # print("integer here", nl.getInteger())
                curr = nl.getInteger()
                self.stack.pop()
            else:
                nums = nl.getList()
                if idx >= len(nums):
                    self.stack.pop()
                    # print("remove from stack", len(self.stack))
                    continue
                self.stack[-1][1] = idx + 1
                # print("add to stack", len(self.stack))
                self.stack.append([nums[idx], 0])
        return curr

    def hasNext(self):
        """
        :rtype: bool
        """
        num = self.next()
        if num is not None:
            self.num = num
        return num is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())