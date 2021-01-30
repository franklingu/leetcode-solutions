"""

None
"""


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class FirstUnique:
    def __init__(self, nums: List[int]):
        track = {}
        for n in nums:
            if n not in track:
                track[n] = 1
            else:
                track[n] += 1
        vals = [n for n in nums if track[n] == 1]
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.track = {}
        self.ns = set(track.keys())
        for n in vals:
            node = ListNode(n)
            self.track[n] = node
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node

    def showFirstUnique(self) -> int:
        if not self.track:
            return -1
        return self.head.next.val

    def add(self, value: int) -> None:
        if value in self.ns and value not in self.track:
            return
        if value in self.track:
            node = self.track[value]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.track[value]
            return
        node = ListNode(value)
        self.track[value] = node
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)