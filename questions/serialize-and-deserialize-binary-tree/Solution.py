"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
 
Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [1,2]

 
Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        if root is None:
            return ret
        queue = [root]
        index = -1
        while queue:
            node = queue.pop(0)
            index += 1
            while index >= len(ret):
                ret.append('null')
            if node is None:
                continue
            ret[index] = str(node.val)
            queue.append(node.left)
            queue.append(node.right)
        while ret and ret[-1] == 'null':
            ret.pop()
        return '[{0}]'.format(','.join(ret))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = self.convert_to_list(data)
        if not data:
            return None
        root = None
        queue = [(None, True)]
        index = -1
        while queue:
            prev, is_left = queue.pop(0)
            index += 1
            if index >= len(data) or data[index] is None:
                continue
            node = TreeNode(data[index])
            if prev is not None:
                if is_left:
                    prev.left = node
                else:
                    prev.right = node
            if root is None:
                root = node
            queue.append((node, True))
            queue.append((node, False))
        return root
    
    def convert_to_list(self, data):
        ret = []
        seen = []
        for c in data:
            if c == '[':
                continue
            elif c == ']':
                continue
            elif c == ',':
                if seen and seen[0] == 'n':
                    ret.append(None)
                else:
                    ret.append(int(''.join(seen)))
                seen = []
            else:
                seen.append(c)
        if seen:
            if seen[0] == 'n':
                ret.append(None)
            else:
                ret.append(int(''.join(seen)))
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))