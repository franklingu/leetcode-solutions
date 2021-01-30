"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def find_neighbors(curr, wordList):
            for index in range(len(curr)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = curr[:index] + ch + curr[index+1:]
                    if nextWord in wordList:
                        yield nextWord
        
        wordList = set(wordList)
        if beginWord in wordList:
            wordList.remove(beginWord)
        if endWord not in wordList:
            return 0
        queue = collections.deque([[beginWord, 1]])
        visited = set()
        while queue:
            curr, step = queue.popleft()
            if curr == endWord:
                return step
            if curr != beginWord and curr not in wordList:
                continue
            if curr != beginWord:
                wordList.remove(curr)
            for neighbor in find_neighbors(curr, wordList):
                queue.append((neighbor, step + 1))
        return 0