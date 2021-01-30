"""

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
 
Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086

 
Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000


"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        l = []
        for i, c in enumerate(costs):
            l.append((c[0] - c[1], i))
        l.sort(key=lambda x: -abs(x[0]))
        first = set()
        second = set()
        for e in l:
            if e[0] <= 0 and len(first) < len(l) // 2:
                first.add(e[1])
            elif e[0] >= 0 and len(second) < len(l) // 2:
                second.add(e[1])
            elif e[0] <= 0:
                second.add(e[1])
            else:
                first.add(e[1])
        # print(l, first, second)
        s = 0
        for i, c in enumerate(costs):
            if i in first:
                s += c[0]
            else:
                s += c[1]
        return s