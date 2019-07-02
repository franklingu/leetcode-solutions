'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

'''
Heap
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        hp = []
        nodes = list(lists)
        for idx in range(len(nodes)):
            node = nodes[idx]
            if node is not None:
                hp.append((node.val, idx))
        heapq.heapify(hp)
        head = None
        prev = None
        while hp:
            val, idx = heapq.heappop(hp)
            node = nodes[idx]
            if head is None:
                head = node
            if prev is not None:
                prev.next = node
            ne = node.next
            if ne is not None:
                heapq.heappush(hp, (ne.val, idx))
                nodes[idx] = ne
            prev = node
        return head
