"""

Implement a data structure supporting the following operations:


Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".



Challenge: Perform all these in O(1) time complexity.

"""


class Node:
    def __init__(self, val, count=0):
        self.val = val
        self.count = count
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.track = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.track:
            node = Node(key, 1)
            self.track[key] = node
            nn = self.head.next
            self.head.next = node
            node.prev = self.head
            nn.prev = node
            node.next = nn
        else:
            node = self.track[key]
            node.count += 1
            curr = node
            while curr.next.count is not None and curr.count > curr.next.count:
                prev = curr.prev
                nn = curr.next
                curr.next = nn.next
                nn.next.prev = curr
                curr.prev = nn
                nn.next = curr
                nn.prev = prev
                prev.next = nn

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.track:
            return
        node = self.track[key]
        if node.count == 1:
            prev = node.prev
            nn = node.next
            prev.next = nn
            nn.prev = prev
        else:
            node.count -= 1
            curr = node
            while curr.prev.count is not None and curr.count < curr.prev.count:
                prev = curr.prev
                nn = curr.next
                curr.prev = prev.prev
                prev.prev.next = curr
                curr.next = prev
                prev.prev = curr
                nn.prev = prev
                prev.next = nn
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        ret = self.tail.prev.val
        if ret is None:
            return ''
        return ret

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        ret = self.head.next.val
        if ret is None:
            return ''
        return ret


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()