"""

Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
 
Example 1:

Input
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

Explanation
// cnt(x) = the use counter for key x
// cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // return 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // return -1 (not found)
lfu.get(3);      // return 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // return 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3

 
Constraints:

0 <= capacity, key, value <= 104
At most 105 calls will be made to get and put.

 
Follow up: Could you do both operations in O(1) time complexity? 
"""


from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key = None, value = None, freq = None):
        self.val = value
        self.key = key
        self.freq = freq

class LFUCache:

    def __init__(self, capacity: int):
        self.freqNodes = defaultdict(OrderedDict)
        self.nodes = {}
        self.minFreq = 0
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if self.capacity > 0 and key in self.nodes:
            node = self._update(key)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        # Update an existing node
        if key in self.nodes:
            node = self._update(key)
            node.val = value
        # Add a new node
        else:            
            node = Node(key, value, 1)
            self.nodes[key] = node
            
            if len(self.nodes) > self.capacity:
                _, delNode = self.freqNodes[self.minFreq].popitem(last=False)
                del self.nodes[delNode.key]
                del delNode

            self.minFreq = 1
            self.freqNodes[1][key] = node
            
    def _update(self, key):
        node = self.nodes[key]
        
        # Remove it from the OrderedDict with the previous frequency
        if len(self.freqNodes[node.freq]) == 1:
            del self.freqNodes[node.freq][key]
            del self.freqNodes[node.freq]
            if self.minFreq == node.freq:
                self.minFreq += 1
        else:
            del self.freqNodes[node.freq][key]
        
        # Increment the frequency of the node and add it to the Ordered Dict with the new frequency
        node.freq += 1
        self.freqNodes[node.freq][key] = node
        
        return node


class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LFUCache2:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        node.val[0] += 1
        node.prev.next = node.next
        node.next.prev = node.prev
        self._move_node(node)
        # self._debug()
        return node.val[1]
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.map:
            node = self.map[key]
            node.val[0] += 1
            node.val[1] = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self._move_node(node)
            return
        if len(self.map) == self.capacity:
            curr = self.tail.prev
            while curr.prev != self.head:
                if curr.val[0] < curr.prev.val[0]:
                    break
                curr = curr.prev
            k = curr.val[2]
            del self.map[k]
            curr.prev.next, curr.next.prev = curr.next, curr.prev
        node = ListNode([1, value, key])
        prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        prev.next = node
        node.prev = prev
        self.map[key] = node
        # self._debug()
    
    def _move_node(self, node):
        while node.prev != self.head:
            if node.val[0] <= node.prev.val[0]:
                break
            node.prev, node.next = node.prev.prev, node.prev
        node.prev.next = node
        node.next.prev = node
    
    def _debug(self):
        print(self.map.keys())
        ls = []
        curr = self.head
        while curr:
            ls.append(curr.val)
            curr = curr.next
        print(ls)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
