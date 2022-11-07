"""

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.

There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
Note that the starting point is assumed to be valid, so it might not be included in the bank.
 
Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

 
Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].


"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def checkNeighbor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]]) == 1
        
        ### initialize the q with start and 0 mutations
        q = deque([[start,0]])
        ### initialize the visited set with start
        visited = {start}
        while q:
            cur, mutations = q.popleft()
            ### if cur == end, we are done
            if cur == end:
                return mutations
            ### go through all gene mutations from the bank
            for nei in bank:
                ### check if nei is a valid neighbor and if we have visited it before
                ### if not, we add it to the visited, add it to the q with mutations+1
                if checkNeighbor(cur,nei) and nei not in visited:
                    visited.add(nei)
                    q.append([nei,mutations+1])
        ### if we don't reach the end, there is no such a mutation, return -1
        return -1