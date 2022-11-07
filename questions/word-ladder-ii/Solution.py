"""

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
 
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 
Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
The sum of all shortest transformation sequences does not exceed 105.


"""


"""
In a nutshell, this problem is an advanced graph traversal algorithm. Here, we use BFS to find all shortest paths
from beginWord to endWord in a constructed graph  g = (V, E). 
	- |V| = k+1 if beginWord is not in wordList and |V| = k otherwise.
	- an edge (u, v) is in E if and only if wordList[u] and wordList[v] differ by exactly one character.
Check the docstrings for all the necessary methods for an in-depth explanation of this modified BFS algorithm.
"""

from typing import List
import math

def differ(str1, str2):
	"""
	determines if two strings differ by one character.
	"""
	diff = 0

	for i in range(len(str1)):
		if str1[i] != str2[i]:
			diff += 1

	return diff == 1


def convert(words):
	"""
	converts words into the adjacency list representation of a graph, as detailed above.
	"""
	edges = []
	graph = [[] for _ in range(len(words))]

	for i in range(len(words)):
		for j in range(i, len(words)):
			if differ(words[i], words[j]):
				edges.append([i, j])

	for pair in edges:
		graph[pair[0]].append(pair[1])
		graph[pair[1]].append(pair[0])

	return graph


def bfs(graph, start):
	"""
	performs a modified bfs search on graph with start node start.

	Returns:
		- parents, a dictionary that maps each node in the graph to a list of parents that have the shortest distance from the start node.

	start is the index such that wordList[start] = beginWord
	"""
	dist = {start: 0}  # dictionary that maps each node in graph to the shortest distance away from start.
	parents = {start: None}

	for i in range(len(graph)):
		if i != start:
			dist[i] = math.inf
			parents[i] = []

	queue = [start]

	while queue:
		node = queue.pop()

		for neighbor in graph[node]:
			if dist[neighbor] == math.inf:  # neighbor has not been visited yet
				dist[neighbor] = dist[node] + 1
				parents[neighbor].append(node)
				queue.insert(0, neighbor)

			else:  # neighbor has been visited!
				if dist[node] + 1 == dist[neighbor]:
					parents[neighbor].append(node)
				elif dist[node] + 1 < dist[neighbor]:  # found a quicker path to neighbor
					dist[neighbor] = dist[node] + 1
					parents[neighbor].clear()
					parents[neighbor].append(node)

	return parents


def findPaths(pathList, currPath, currNode, parents, wordList):
	"""
	traces back to find all paths from the end node to the start node given the parents dictionary. Returns nothing,
	but modifies the input pathList to include all possible paths.
	"""
	if parents[currNode] is None:
		currPath.reverse()
		pathList.append(currPath)

	if parents[currNode]:
		for parent in parents[currNode]:
			findPaths(pathList, currPath + [wordList[parent]], parent, parents, wordList)


class Solution:
	def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
		if beginWord not in wordList:
			wordList.append(beginWord)

		if endWord not in wordList:
			return []

		endIndex = wordList.index(endWord)
		beginIndex = wordList.index(beginWord)

		graph = convert(wordList)
		parents = bfs(graph, beginIndex)

		pathList = []
		currPath = [endWord]
		findPaths(pathList, currPath, endIndex, parents, wordList)

		return pathList