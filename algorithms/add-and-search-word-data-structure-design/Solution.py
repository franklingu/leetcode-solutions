"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class TrieNode:
    def __init__(self):
        self.track = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for ch in word:
            if ch in curr.track:
                ne = curr.track[ch]
            else:
                ne = TrieNode()
                curr.track[ch] = ne
            curr = ne
        curr.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        stack = [(curr, 0)]
        while stack:
            curr, index = stack.pop()
            if index == len(word) - 1:
                if word[index] == '.':
                    for ch, ne in curr.track.items():
                        if ne.end:
                            return True
                else:
                    if curr.track.get(word[index]) and curr.track[word[index]].end:
                        return True
                continue
            if word[index] != '.' and word[index] not in curr.track:
                continue
            if word[index] == '.':
                for ch, ne in curr.track.items():
                    stack.append((ne, index + 1))
            else:
                stack.append((curr.track[word[index]], index + 1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
