"""

Design an algorithm that accepts a stream of characters and checks if a suffix of these characters is a string of a given array of strings words.
For example, if words = ["abc", "xyz"] and the stream added the four characters (one by one) 'a', 'x', 'y', and 'z', your algorithm should detect that the suffix "xyz" of the characters "axyz" matches "xyz" from words.
Implement the StreamChecker class:

StreamChecker(String[] words) Initializes the object with the strings array words.
boolean query(char letter) Accepts a new character from the stream and returns true if any non-empty suffix from the stream forms a word that is in words.

 
Example 1:

Input
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
Output
[null, false, false, false, true, false, true, false, false, false, false, false, true]

Explanation
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // return False
streamChecker.query("b"); // return False
streamChecker.query("c"); // return False
streamChecker.query("d"); // return True, because 'cd' is in the wordlist
streamChecker.query("e"); // return False
streamChecker.query("f"); // return True, because 'f' is in the wordlist
streamChecker.query("g"); // return False
streamChecker.query("h"); // return False
streamChecker.query("i"); // return False
streamChecker.query("j"); // return False
streamChecker.query("k"); // return False
streamChecker.query("l"); // return True, because 'kl' is in the wordlist

 
Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 200
words[i] consists of lowercase English letters.
letter is a lowercase English letter.
At most 4 * 104 calls will be made to query.


"""


# Implement Trie tree use Hashtable
class TrieTree:
    def __init__(self):
        self.root = {}
    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            if word[i] in node:
                node = node[word[i]]
                i += 1
                continue
            break        
        while i < len(word):
            node[word[i]] = {}
            node = node[word[i]]
            i+=1
		# mark it as the last character of a word
        node["$"]={}
        return
     # Check whether the stream suffix existed on tree or not
	 # Can reverse suffix, so we check it like prefix
    def isPrefix(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            if "$" in node[c]:
                return True
            node = node[c]
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = ""
        self.trie = TrieTree()
        for w in words:
			# because we need to check suffix, so reversing the word
            self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.stream += letter
        return self.trie.isPrefix(self.stream[::-1])
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)