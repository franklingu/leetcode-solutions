"""

None
"""


from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.ss = ''
        self.root = TrieNode()
        for sentence, time in zip(sentences, times):
            self.add_input(sentence, time)
    
    def add_input(self, sentence, time):
        curr = self.root
        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.words[sentence] += time

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.ss = self.ss + c
        else:
            self.add_input(self.ss, 1)
            self.ss = ''
            return []
        curr = self.root
        for ch in self.ss:
            if ch not in curr.children:
                curr = None
                break
            curr = curr.children[ch]
        ret = []
        if curr is not None:
            ret = [x[0] for x in list(sorted(curr.words.items(), key=lambda x: (-x[1], x[0])))[:3]]
        return ret


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)