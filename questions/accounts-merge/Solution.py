"""

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts.  Two accounts definitely belong to the same person if there is some email that is common to both accounts.  Note that even if two accounts have the same name, they may belong to different people as people could have the same name.  A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.  The accounts themselves can be returned in any order.
Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.


Note:
The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def get_connections(accounts):
            track = {}
            emails = {}
            for i, acc in enumerate(accounts):
                if i not in track:
                    track[i] = []
                for j, email in enumerate(acc):
                    if j == 0:
                        continue
                    if email not in emails:
                        emails[email] = []
                    for k in emails[email]:
                        if k not in track:
                            track[k] = []
                        track[k].append(i)
                        track[i].append(k)
                    emails[email].append(i)
            return track
        
        track = get_connections(accounts)
        visited = set()
        parts = []
        for i, acc in enumerate(accounts):
            if i in visited:
                continue
            part = []
            stack = [i]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                part.append(curr)
                for ne in track.get(curr, []):
                    if ne in visited:
                        continue
                    stack.append(ne)
            parts.append(part)
        ret = []
        for part in parts:
            name = accounts[part[0]][0]
            acc = set()
            for pp in part:
                acc = acc.union(set(accounts[pp][1:]))
            ret.append([name] + sorted(acc))
        return ret