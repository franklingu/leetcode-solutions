"""
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)



 Example 1:

 Input: people = [1,2], limit = 3
 Output: 1
 Explanation: 1 boat (1, 2)
 Example 2:

 Input: people = [3,2,2,1], limit = 3
 Output: 3
 Explanation: 3 boats (1, 2), (2) and (3)
 Example 3:

 Input: people = [3,5,3,4], limit = 5
 Output: 4
 Explanation: 4 boats (3), (3), (4), (5)
 Note:

 1 <= people.length <= 50000
 1 <= people[i] <= limit <= 30000

"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        if len(people) < 2 or limit < people[1] + people[0]:
            return len(people)
        last_idx = len(people) - 1
        start_idx = 0
        boats = 0
        while last_idx >= start_idx:
            num = limit - people[last_idx]
            last_idx -= 1
            if start_idx <= last_idx and num >= people[start_idx]:
                num -= people[start_idx]
                start_idx += 1
            boats += 1
        return boats

