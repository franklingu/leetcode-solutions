'''
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

![Image0](https://assets.leetcode.com/uploads/2018/12/13/160_statement.png)

begin to intersect at node c1.

 

Example 1:

![Image1](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:

![Image2](https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png)

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:

![Image3](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def findEndOfList(node):
            prev, curr = None, node
            l = 0
            while curr is not None:
                l += 1
                prev = curr
                curr = curr.next
            return l, prev
        
        def advance(node, l):
            while l > 0:
                node = node.next
                l -= 1
            return node
        
        l1, e1 = findEndOfList(headA)
        l2, e2 = findEndOfList(headB)
        if not(e1 == e2 and e1 is not None and e2 is not None):
            return None
        h1 = headA
        h2 = headB
        if l1 > l2:
            h1 = advance(h1, l1 - l2)
        elif l2 > l1:
            h2 = advance(h2, l2 - l1)
        while h1 is not None:
            if h1 == h2:
                return h1
            h1 = h1.next
            h2 = h2.next
        return None
