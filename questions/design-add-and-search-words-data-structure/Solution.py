"""

Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 
Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

 
Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.


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