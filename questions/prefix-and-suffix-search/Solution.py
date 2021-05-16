"""

Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.
Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

 
Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".

 
Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.


"""


class Trie:
    def __init__(self):
        self.dd = {}
        self.idc = set()
    
    def add(self, word, index):
        prefix = ''
        for c in list(word):
            prefix += c
            if prefix not in self.dd:
                self.dd[prefix] = set()
            self.dd[prefix].add(index)
        self.idc.add(index)
            
    
    def match(self, prefix):
        if len(prefix) == 0:
            return self.idc
        return self.dd.get(prefix, set())

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_trie = Trie()
        self.suffix_trie = Trie()
        visited = set()
        for i, word in enumerate(reversed(words)):
            if word in visited:
                continue
            visited.add(word)
            index = len(words) - i - 1
            self.prefix_trie.add(word, index)
            self.suffix_trie.add(word[::-1], index)

    def f(self, prefix: str, suffix: str) -> int:
        pm = self.prefix_trie.match(prefix)
        sm = self.suffix_trie.match(suffix[::-1])
        ret = list(pm.intersection(sm))
        if not ret:
            return -1
        return max(ret)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)