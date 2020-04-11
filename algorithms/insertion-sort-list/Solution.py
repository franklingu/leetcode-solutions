"""
Sort a linked list using insertion sort.

![img](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        def insert(sl, node):
            if sl is None:
                return node
            prev, curr = None, sl
            while curr is not None and curr.val < node.val:
                prev = curr
                curr = curr.next
            if prev is None:
                node.next = sl
                return node
            prev.next = node
            node.next = curr
            return sl
            
        
        sl = None
        curr = head
        while curr is not None:
            nn = curr.next
            curr.next = None
            sl = insert(sl, curr)
            curr = nn
        return sl
