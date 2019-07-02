'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

'''
LRU can be implemented with doubly linked list and hashmap
'''


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete_node(node)
        self.insert_after_head(node)
        return node.val
    
    def delete_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def insert_after_head(self, node: ListNode) -> None:
        second = self.head.next
        self.head.next = node
        node.next = second
        second.prev = node
        node.prev = self.head

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            self.cache[key].val = value
            return
        if len(self.cache) >= self.capacity:
            second_last = self.tail.prev
            self.delete_node(second_last)
            del self.cache[second_last.key]
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert_after_head(node)
    
    def debug(self):
        curr = self.head.next
        print(self.cache)
        while curr != self.tail:
            print(curr.key, curr.val, end='   ')
            curr = curr.next
        print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
