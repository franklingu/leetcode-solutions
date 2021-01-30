"""

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
Follow up: Could you do this in O(n) runtime?
 
Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0

Example 3:

Input: nums = [2,4]
Output: 6

Example 4:

Input: nums = [8,10,2]
Output: 10

Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

 
Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1


"""


# class Solution:
#     def findMaximumXOR(self, nums: List[int]) -> int:
#         def fill_trie(trie, num):
#             curr = trie
#             for i in range(31, -1, -1):
#                 bit = (num >> i) & 1
#                 if bit not in curr:
#                     curr[bit] = {}
#                 curr = curr[bit]
        
#         def find_max(trie):
#             res = [0] * 32
#             queue = [(trie.get(0), trie.get(1))]
#             index = 0
#             while queue:
#                 newq = []
#                 val = 0
#                 for elem in queue:
#                     zero, one = elem
#                     if zero is None and one is None:
#                         continue
#                     elif zero is None or one is None:
#                         if val > 0:
#                             continue
#                     else:
#                         val = 1
#                 for elem in queue:
#                     zero, one = elem
#                     if one is None and zero is None:
#                         continue
#                     if zero is None and val == 0:
#                         newq.append((one.get(0), one.get(1)))
#                     if one is None and val == 0:
#                         newq.append((zero.get(0), zero.get(1)))
#                     if zero is not None and one is not None and val == 1:
#                         newq.append((one.get(0), zero.get(1)))
#                         newq.append((zero.get(0), one.get(1)))
#                 if index < len(res):
#                     res[index] = val
#                 index += 1
#                 queue = newq
#                 print(res)
#             num = 0
#             for n in res:
#                 num = (num << 1) + n
#             return num
            
#         trie = {}
#         for num in nums:
#             fill_trie(trie, num)
#         return find_max(trie)

class TrieNode():
    def __init__(self):
        self.one = None
        self.zero = None

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            node = root
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero
                    
        ans = 0
        for num in nums:
            node = root
            tmp_val = 0
            for j in range (31, -1, -1):
                tmp = num & 1 << j
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << j
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << j
                    node = node.one or node.zero
            ans = max(ans, tmp_val)
                                                
        return ans